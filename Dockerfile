from python:3.7.4
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
ADD src/api /code/api
ADD src/crawler /code/api/crawler
ENV FLASK_APP api/app.py
ENTRYPOINT gunicorn -w 4 -b 0.0.0.0:4000 --chdir=api app:app
