from typing import Dict, List

import requests_html


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
        values = row.text.replace('\xa0 ', '').replace(':\n', ':').split('\n')
        for value in values:
            value = value.split(':')
            data.append({value[0]: value[1]})
        result.append(data)
    return result
