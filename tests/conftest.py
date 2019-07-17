import pytest

from requests_html import Element, HTML


@pytest.fixture()
def process() -> HTML:
    doc = ''
    with open('tests/process.html') as f:
        doc = f.read()
    html = HTML(html=doc)
    return html


@pytest.fixture
def movements(process: HTML) -> Element:
    return process.find('#tabelaUltimasMovimentacoes', first=True)


@pytest.fixture
def parts(process: HTML) -> Element:
    return process.find('#tableTodasPartes', first=True)
