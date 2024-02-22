#!/bin/bash

su - NSTM -c "git -C ~/nstm pull origin master"

migrations="$(/home/NSTM/venv/bin/python /home/NSTM/NSTM/manage.py showmigrations --plan | grep -v '\[X\]')"

if [[ $migrations = *[!\ ]* ]]; then
  githash="$(git -C /home/NSTM/NSTM rev-parse --short HEAD^1)"
  now=`date +%Y%m%d%H%M%S`
  dumpfile="nstm_db_backup_${githash}_${now}.sql"
  su - postgres -c "pg_dump nstm > ${dumpfile}"
  echo "Created database backup (${dumpfile}) due to changes on schema."
else
  echo "Skipped backup. No changes on the database schema."
fi

su - NSTM -c "~/venv/bin/pip install -r ~/nstm/requirements.txt"
su - NSTM -c "~/venv/bin/python ~/nstm/manage.py migrate"
su - NSTM -c "~/venv/bin/python ~/nstm/manage.py collectstatic --noinput"

sudo supervisorctl restart nstm_gunicorn
sudo supervisorctl restart nstm_celery_worker
sudo supervisorctl restart nstm_celery_beat

exit 0
