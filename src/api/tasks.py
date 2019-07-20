from celery_app import celery_app
from crawler import crawlers, parsers
from models import db, RawHTML, Process


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

    page = ''
    identify = process_number[-9:-5]
    method = methods.get((grade, identify))
    page = method(process_number)
    raw_html = RawHTML(process_number=process_number, grade=grade)
    raw_html.html = page
    db.session.add(raw_html)
    db.session.commit()
    parser_task.delay(raw_html.id)


@celery_app.task(queue='parser', exchange='parser',
                 soft_time_limit=30, time_limit=30+10, max_retries=5)
def parser_task(file_id: str):
    raw_html = RawHTML.query.get(file_id)
    parsed_data = parsers.process(raw_html.html)
    process = Process.query.get(raw_html.process_number)
    if raw_html.grade == 1:
        process.grade1 = parsed_data
    elif raw_html.grade == 2:
        process.grade2 = parsed_data
    db.session.add(process)
    db.session.commit()
