from typing import Dict, List

import requests_html


def process(process_data: str) -> Dict:
    process_data = requests_html.HTML(html=process_data)
    result = {'Dados do processo': {}, 'Partes do processo': [],
              'Movimentações': []}
    not_found = ('Não existem informações disponíveis para os '
                 'parâmetros informados')
    if not_found not in process_data.text:
        process_general_data = process_data.xpath(
            "//table[contains(@class, 'secaoFormBody')]")[1]
        result['Dados do processo'] = general_data(process_general_data)

        process_parts = process_data.find(
            '#tableTodasPartes,#tablePartesPrincipais', first=True)
        result['Partes do processo'] = parts(process_parts)

        process_movements = process_data.find(
            '#tabelaUltimasMovimentacoes', first=True)
        result['Movimentações'] = movements(process_movements)
    return result


def movements(process: requests_html.Element) -> List[Dict]:
    rows = process.xpath('//tr')
    result = []
    for row in rows:
        data = []
        for col in row.xpath('//td'):
            data.append(col.text)
        result.append({'data': data[0], 'movimento': ''.join(data[1:])})
    return result


def parts(process_parts: requests_html.Element) -> List[List[Dict]]:
    rows = process_parts.xpath('//tr')
    result = []
    for row in rows:
        data = []
        values = row.text.replace('\xa0', '').replace(':\n', ':').split('\n')
        for value in values:
            value = value.split(':')
            data.append({value[0]: value[1].strip()})
        result.append(data)
    return result


def general_data(process_general_data: requests_html.Element) -> Dict:
    result = {}
    names = ['Classe', 'Área', 'Assunto', 'Distribuição', 'Juiz', 'Relator',
             'Valor da ação']
    for name in names:
        field = process_general_data.xpath(
            f"//tr[contains(string(), '{name}')]", first=True)
        if field:
            field = field.text
            field = field.replace(': ', ':\n')
            field = field.split(':\n')
            result[field[0]] = field[1]
    return result
