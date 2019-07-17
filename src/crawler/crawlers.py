from requests_html import HTMLSession


def get_page_from_first_instance_TJAL(process_number: str):
    url = 'https://www2.tjal.jus.br/cpopg/search.do'
    params = {
        'conversationId': '',
        'dadosConsulta.localPesquisa.cdLocal': -1,
        'cbPesquisa': 'NUMPROC',
        'dadosConsulta.tipoNuProcesso': 'UNIFICADO',
        'numeroDigitoAnoUnificado': process_number[:15],
        'foroNumeroUnificado': process_number[-4:],
        'dadosConsulta.valorConsultaNuUnificado': process_number,
        'dadosConsulta.valorConsulta': '',
        'uuidCaptcha': ''
    }
    return get_page(url, params)


def get_page_from_second_instance_TJAL(process_number: str):
    url = 'https://www2.tjal.jus.br/cposg5/search.do?'
    params = {'conversationId': '',
              'paginaConsulta': 1,
              'cbPesquisa': 'NUMPROC',
              'tipoNuProcesso': 'UNIFICADO',
              'numeroDigitoAnoUnificado': '0710802-55.2018',
              'foroNumeroUnificado': '0001',
              'dePesquisaNuUnificado': '0710802-55.2018.8.02.0001',
              'dePesquisa': '',
              'uuidCaptcha': ''
              }
    return get_page(url, params)


def get_page(url: str, params: dict, timeout=30) -> str:
    session = HTMLSession()
    r = session.get(url, params=params, timeout=timeout)
    return r.html.html
