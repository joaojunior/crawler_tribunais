env PYTHONPATH=src gunicorn -w 4 -b 0.0.0.0:4000 --chdir=src/api app:app_flask
