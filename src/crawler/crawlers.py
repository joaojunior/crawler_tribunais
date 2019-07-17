from requests_html import HTMLSession


def get_page_from_first_instance_TJAL(process_number: str):
    url = 'https://www2.tjal.jus.br/cpopg/search.do'
    params = {
        'cbPesquisa': 'NUMPROC',
        'dadosConsulta.tipoNuProcesso': 'UNIFICADO',
        'numeroDigitoAnoUnificado': process_number[:15],
        'foroNumeroUnificado': process_number[-4:],
        'dadosConsulta.valorConsultaNuUnificado': process_number,
    }
    return get_page(url, params)


def get_page_from_second_instance_TJAL(process_number: str):
    url = 'https://www2.tjal.jus.br/cposg5/search.do?'
    params = {
              'cbPesquisa': 'NUMPROC',
              'tipoNuProcesso': 'UNIFICADO',
              'numeroDigitoAnoUnificado': process_number[:15],
              'foroNumeroUnificado': process_number[-4:],
              'dePesquisaNuUnificado': process_number,
              'pbEnviar': 'Pesquisar'
              }
    return get_page(url, params)


def get_page_from_first_instance_TJMS(process_number: str):
    url = 'https://esaj.tjms.jus.br/cpopg5/search.do'
    params = {
        'cbPesquisa': 'NUMPROC',
        'dadosConsulta.tipoNuProcesso': 'UNIFICADO',
        'numeroDigitoAnoUnificado': process_number[:15],
        'foroNumeroUnificado': process_number[-4:],
        'dadosConsulta.valorConsultaNuUnificado': process_number,
    }
    return get_page(url, params)


def get_page_from_second_instance_TJMS(process_number: str):
    url = 'https://esaj.tjms.jus.br/cposg5/search.do'
    params = {
        'cbPesquisa': 'NUMPROC',
        'tipoNuProcesso': 'UNIFICADO',
        'numeroDigitoAnoUnificado': process_number[:15],
        'foroNumeroUnificado': process_number[-4:],
        'dePesquisaNuUnificado': process_number
    }
    return get_page(url, params)


def get_page(url: str, params: dict, timeout=30) -> str:
    session = HTMLSession()
    r = session.get(url, params=params, timeout=timeout)
    return r.html.html
