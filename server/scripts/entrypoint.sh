#!/bin/sh
set -e

./scripts/wait-for-postgres.sh
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
