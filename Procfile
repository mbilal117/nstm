web: gunicorn nstm.wsgi --log-file -
worker: celery worker --app=nstm --loglevel=INFO
beat: celery beat --app=nstm --loglevel=INFO
