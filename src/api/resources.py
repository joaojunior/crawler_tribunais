from flask_restful import Resource

from models import db, Process
from schemas import ProcessSchema
from tasks import crawler_task


class ProcessResource(Resource):
    TJAL = '8.02'
    TJMS = '8.12'

    def get(self, process_number):
        if len(process_number) != 25:
            return {
                'msg': f'Número do processo {process_number} inválido'}, 422
        identify = process_number[-9:-5]
        if identify != self.TJAL and identify != self.TJMS:
            return {'msg':
                    f'Processo {process_number} não pertence a TJAL ou TJMS'
                    }, 422
        process = Process.query.get(process_number)
        if process is None:
            process = Process(process_number=process_number)
            db.session.add(process)
            db.session.commit()
            crawler_task.delay(process_number, 1)
            crawler_task.delay(process_number, 2)

        process_schema = ProcessSchema()
        return process_schema.jsonify(process)
