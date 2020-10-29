# django-admin compilemessages
# python manage.py runserver 0.0.0.0:8000 --settings=settings.production

# for async web server:
export DJANGO_SETTINGS_MODULE=settings.production
uvicorn recruitment.asgi:application --port 8001 --workers 2
#uvicorn recruitment.asgi:application --port 8001 --workers 2
