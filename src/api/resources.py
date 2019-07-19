from flask_restful import Resource

from crawler import crawlers
from crawler import parsers
from models import db, Process
from schemas import ProcessSchema


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
        process_schema = ProcessSchema()
        process = Process.query.get(process_number)
        if process is not None:
            return process_schema.jsonify(process)
        if identify == self.TJAL:
            page1 = crawlers.get_page_from_first_instance_TJAL(process_number)
            page2 = crawlers.get_page_from_second_instance_TJAL(process_number)
            grade_1 = parsers.process(page1)
            grade_2 = parsers.process(page2)
        elif identify == self.TJMS:
            page1 = crawlers.get_page_from_first_instance_TJMS(process_number)
            page2 = crawlers.get_page_from_second_instance_TJMS(process_number)
            grade_1 = parsers.process(page1)
            grade_2 = parsers.process(page2)
        process = Process(number=process_number, grade1=grade_1,
                          grade2=grade_2)
        db.session.add(process)
        db.session.commit()
        return process_schema.jsonify(process)
