from unittest.mock import Mock, patch

import pytest
from requests.exceptions import ConnectTimeout


from crawler import crawlers


@pytest.mark.parametrize('method', [
    crawlers.get_page_from_first_instance_TJAL,
    crawlers.get_page_from_second_instance_TJAL,
    crawlers.get_page_from_first_instance_TJMS,
    crawlers.get_page_from_second_instance_TJMS])
@patch('crawler.crawlers.HTMLSession')
def test_crawler_response_when_found_process(mock_session, method, process):
    instance = mock_session.return_value
    html_response = Mock(html=process)
    instance.get.return_value = html_response

    expected = process
    process_number = '0821901-51.2018.8.12.0001'
    assert expected.html == method(process_number)


def test_crawler_exceed_timeout_raise_error():
    url = 'https://esaj.tjms.jus.br/cposg5/search.do'

    with pytest.raises(ConnectTimeout):
        crawlers.get_page(url, {}, timeout=0.001)
