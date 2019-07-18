from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api

from crawler import crawlers
from crawler import parsers


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
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
        elif identify == self.TJAL:
            page1 = crawlers.get_page_from_first_instance_TJAL(process_number)
            page2 = crawlers.get_page_from_second_instance_TJAL(process_number)
            grade_1 = parsers.process(page1)
            grade_2 = parsers.process(page2)
        elif identify == self.TJMS:
            page1 = crawlers.get_page_from_first_instance_TJMS(process_number)
            page2 = crawlers.get_page_from_second_instance_TJMS(process_number)
            grade_1 = parsers.process(page1)
            grade_2 = parsers.process(page2)
        return jsonify({'Número do processo': process_number,
                        '1 Grau': grade_1,
                        '2 Grau': grade_2})


api.add_resource(HelloWorld, '/<string:process_number>')

if __name__ == '__main__':
    app.run(debug=True)
