#!/bin/sh

set -e

DJANGO_PORT=8000
DJANGO_ADMIN_EMAIL=${APP_ADMIN_EMAIL:='admin@rindus.com'}
DJANGO_ADMIN_PASSWORD=${APP_ADMIN_PASSWORD:='rindus2019'}



create_super_user(){
cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()

User.objects.create_superuser('${DJANGO_ADMIN_EMAIL}', '${DJANGO_ADMIN_PASSWORD}') if User.objects.filter(username='${DJANGO_ADMIN_USER}').exists()
EOF
}




migrations(){
    python manage.py makemigrations --noinput
    python manage.py migrate --noinput
}

runtest(){
    python manage.py test
}



system_setup(){
    migrations
    runtest
    create_super_user
}

system_setup
exec python manage.py runserver 0.0.0.0:"${DJANGO_PORT}"


exec $@