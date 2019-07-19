from python:3.7.4
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
ADD src/api /code/src/api
ADD scripts/db.sh /code/src/api
ADD src/crawler /code/src/crawler
ADD tests /code/tests
ENV FLASK_APP api/app.py
ENTRYPOINT env PYTHONPATH=src gunicorn -w 4 -b 0.0.0.0:4000 --chdir=src/api app:app
