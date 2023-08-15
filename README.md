# installation_calculation
Small Django is a project for easily counting from a downloaded excel spreadsheet \
- from use this calc you must install all packets in requirements.txt \
- create django database
  - `python3 manage.py makemigrations`
  - `python3 manage.py migrate`
  - `python3 manage.py createsuperuser`
- if you want, create service from work 24/7 \
 manual to configure (https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru)
- start gunicorn server  with you ip
- when your server up, database is empty, you must import  template price.xlsx on site



