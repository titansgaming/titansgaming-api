FROM python:3.6-slim

WORKDIR /srv
COPY . /srv

RUN pip3 install -r /srv/requirements.txt

RUN python3 manage.py collectstatic
RUN python3 manage.py migrate

EXPOSE 80
CMD gunicorn --bind 0.0.0.0:80 titansgaming.wsgi
