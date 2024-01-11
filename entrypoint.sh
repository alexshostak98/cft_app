#!/bin/sh

CONTAINER_FIRST_STARTUP="CONTAINER_FIRST_STARTUP"
if [ ! -e /$CONTAINER_FIRST_STARTUP ]; then
    touch /$CONTAINER_FIRST_STARTUP
    python manage.py migrate &&
    python manage.py fill_credit_application_table &&
    python manage.py fill_producer_table &&
    python manage.py fill_contract_table &&
    python manage.py fill_product_table &&
    python manage.py createsuperuser --username 'admin' --email 'admin@mail.com' --noinput &&
    python manage.py runserver 0.0.0.0:8081
else
    python manage.py runserver 0.0.0.0:8081
fi