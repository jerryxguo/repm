cd C:\workspace\django\open\repm\
python manage.py process_tasks
set year=%date:~-6,2%
set month=%date:~3,2%
set day=%date:~0,2%
COPY db.sqlite3  db.sqlite3_%year%_%month%_%day%