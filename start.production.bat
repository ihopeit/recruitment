django-admin compilemessages
# python manage.py runserver 0.0.0.0:8000 --settings=settings.production

# for async web server:
export DJANGO_SETTINGS_MODULE=settings.production
uvicorn recruitment.asgi:application --workers 3