import os

import pytest
from requests_html import HTML, Element

FIXTURE_DIR = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture()
def process() -> HTML:
    doc = ''
    with open(os.path.join(FIXTURE_DIR, 'process.html')) as f:
        doc = f.read()
    html = HTML(html=doc)
    return html


@pytest.fixture()
def second_process() -> HTML:
    doc = ''
    with open(os.path.join(FIXTURE_DIR, 'process_second.html')) as f:
        doc = f.read()
    html = HTML(html=doc)
    return html


@pytest.fixture()
def process_not_found() -> HTML:
    doc = ''
    with open(os.path.join(FIXTURE_DIR, 'process_not_found.html')) as f:
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


@pytest.fixture
def second_general_data(second_process: HTML) -> Element:
    return second_process.xpath(
        "//table[contains(@class, 'secaoFormBody')]")[1]
