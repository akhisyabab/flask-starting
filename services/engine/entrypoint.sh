#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z engine-db 5432; do
  sleep 0.1
done

flask db upgrade
flask run -h 0.0.0.0
#gunicorn --bind :5000 --chdir ./ manage:application
