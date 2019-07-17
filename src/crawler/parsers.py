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
