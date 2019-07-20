from python:3.7.4
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD requirements.txt /code
ADD requirements_tests.txt /code
RUN pip install -r requirements.txt
ADD src/api /code/src/api
ADD scripts/db.sh /code/src/api
ADD scripts/wait_components.sh /code
ADD scripts/install_wait_components.sh /code
ADD scripts/run_api.sh /code
ADD src/crawler /code/src/crawler
ADD src/api/migrations /code/migrations
ADD tests /code/src/api/tests
ENV DOCKERIZE_VERSION 'v0.6.1'
RUN sh install_wait_components.sh
ENTRYPOINT sh run_api.sh
