import pytest

from requests_html import Element, HTML


@pytest.fixture()
def process() -> HTML:
    doc = ''
    with open('tests/process.html') as f:
        doc = f.read()
    html = HTML(html=doc)
    return html


@pytest.fixture()
def second_process() -> HTML:
    doc = ''
    with open('tests/process_second.html') as f:
        doc = f.read()
    html = HTML(html=doc)
    return html


@pytest.fixture()
def process_not_found() -> HTML:
    doc = ''
    with open('tests/process_not_found.html') as f:
        doc = f.read()
    html = HTML(html=doc)
    return html


@pytest.fixture
def movements(process: HTML) -> Element:
    return process.find('#tabelaUltimasMovimentacoes', first=True)


@pytest.fixture
def second_movements(second_process: HTML) -> Element:
    return second_process.find('#tabelaUltimasMovimentacoes', first=True)


@pytest.fixture
def parts(process: HTML) -> Element:
    return process.find('#tableTodasPartes', first=True)


@pytest.fixture
def second_parts(second_process: HTML) -> Element:
    return second_process.find('#tablePartesPrincipais', first=True)


@pytest.fixture
def general_data(process: HTML) -> Element:
    return process.xpath("//table[contains(@class, 'secaoFormBody')]")[1]
