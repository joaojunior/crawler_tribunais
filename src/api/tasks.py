from celery.utils.log import get_task_logger
from requests.exceptions import ConnectTimeout

from celery_app import celery_app
from crawler import crawlers, parsers
from models import db, RawHTML, Process


logger = get_task_logger(__name__)


@celery_app.task(queue='crawler', exchange='crawler',
                 soft_time_limit=60, time_limit=60+10, max_retries=5)
def crawler_task(process_number: str, grade: int):
    TJAL = '8.02'
    TJMS = '8.12'
    methods = {
        (1, TJAL): crawlers.get_page_from_first_instance_TJAL,
        (2, TJAL): crawlers.get_page_from_second_instance_TJAL,
        (1, TJMS): crawlers.get_page_from_first_instance_TJMS,
        (2, TJMS): crawlers.get_page_from_second_instance_TJMS,
    }

    try:
        identify = process_number[-9:-5]
        method = methods.get((grade, identify))
        page = method(process_number)
        raw_html = RawHTML(process_number=process_number, grade=grade)
        raw_html.html = page
        db.session.add(raw_html)
        db.session.commit()
        parser_task.delay(raw_html.id)
    except ConnectTimeout:
        logger.info(f'Timeout when crawler the process: {process_number}')
    except Exception as error:
        logger.error(f'Error during crawler the process: {process_number}',
                     exc_info=True)
        raise error


@celery_app.task(queue='parser', exchange='parser',
                 soft_time_limit=30, time_limit=30+10, max_retries=5)
def parser_task(file_id: str):
    try:
        raw_html = RawHTML.query.get(file_id)
        parsed_data = parsers.process(raw_html.html)
        process = Process.query.get(raw_html.process_number)
        if raw_html.grade == 1:
            process.grade1 = parsed_data
        elif raw_html.grade == 2:
            process.grade2 = parsed_data
        db.session.add(process)
        db.session.commit()
    except (KeyError, IndexError):
        logger.info((f'file:{file_id},process:{process.process_number}: '
                     f'Error acessing some keys'),
                    exc_info=True)
    except Exception as error:
        logger.error(f'Error during parser the file: {file_id}',
                     exc_info=True)
        raise error
