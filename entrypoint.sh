#!/bin/sh
set -e

# Daftarkan cron job dari django-crontab ke system cron
python manage.py crontab add

# Jalankan cron daemon di background
service cron start

# Jalankan aplikasi Django
exec "$@"
