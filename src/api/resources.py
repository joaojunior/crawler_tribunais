from flask_restful import Resource

from models import db, Process
from schemas import ProcessSchema
from tasks import crawler_task


class ProcessResource(Resource):
    def get(self, process_number):
        if self._process_number_is_valid(process_number) is False:
            return {
                'msg': f'Número do processo {process_number} inválido'}, 422
        process = Process.query.get(process_number)
        if process is None:
            process = Process(process_number=process_number)
            db.session.add(process)
            db.session.commit()
            crawler_task.delay(process_number, 1)
            crawler_task.delay(process_number, 2)

        process_schema = ProcessSchema()
        return process_schema.jsonify(process)

    @staticmethod
    def _process_number_is_valid(process_number: str) -> bool:
        if len(process_number) != 25:
            return False
        try:
            final = process_number.find('.')
            digits = int((process_number[8:final]).replace('-', ''))
            calculated_process_number = (f'{process_number[:8]}'
                                         f'{process_number[final:]}00')
            calculated_process_number = int(calculated_process_number.replace(
                '.', '').replace('-', ''))
            digits_calculated = 98 - (calculated_process_number % 97)
        except Exception:
            return False
        return digits == digits_calculated
