from unittest.mock import Mock, patch


def test_process_number_invalid(client):
    process_number = '2'

    r = client.get(f'/{process_number}')

    expected = {'msg': f'Número do processo {process_number} inválido'}
    assert 422 == r.status_code
    assert expected == r.json


def test_process_not_pertence_tjal_and_tjms(client):
    process_number = '0710802-55.2018.9.12.0001'

    r = client.get(f'/{process_number}')

    expected = {'msg':
                f'Processo {process_number } não pertence a TJAL ou TJMS'}
    assert 422 == r.status_code
    assert expected == r.json


@patch('crawler.crawlers.HTMLSession')
def test_process_pertence_tjal(mock_session, process, client):
    instance = mock_session.return_value
    html_response = Mock(html=process)
    instance.get.return_value = html_response

    process_number = '0710802-55.2018.8.02.0001'

    r = client.get(f'/{process_number}')

    assert 200 == r.status_code


@patch('crawler.crawlers.HTMLSession')
def test_process_pertence_tjms(mock_session, process, client):
    instance = mock_session.return_value
    html_response = Mock(html=process)
    instance.get.return_value = html_response

    process_number = '0710802-55.2018.8.12.0001'

    r = client.get(f'/{process_number}')
    assert 200 == r.status_code
