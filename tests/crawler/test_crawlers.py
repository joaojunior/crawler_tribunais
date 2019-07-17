from unittest.mock import Mock, patch

import pytest


from crawler import crawlers


@pytest.mark.parametrize('method', [
    crawlers.get_page_from_first_instance_TJAL,
    crawlers.get_page_from_second_instance_TJAL])
@patch('crawler.crawlers.HTMLSession')
def test_crawler_response_when_found_process(mock_session, method, process):
    instance = mock_session.return_value
    html_response = Mock(html=process)
    instance.get.return_value = html_response

    expected = process
    process_number = '0821901-51.2018.8.12.0001'
    assert expected.html == method(process_number)
