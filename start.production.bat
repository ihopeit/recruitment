# django-admin compilemessages
# --settings=settings.production
python manage.py runserver 0.0.0.0:8000 $server_params

# for async web server:
#export DJANGO_SETTINGS_MODULE=settings.production
#uvicorn recruitment.asgi:application --port 8000 --workers 2

## TODO fix Dockerfile for production in asyncio.py :
##File "/usr/local/lib/python3.9/site-packages/django/utils/asyncio.py", line 24, in inner
##    raise SynchronousOnlyOperation(message)
## django.core.exceptions.SynchronousOnlyOperation: You cannot call this from an async context - use a thread or sync_to_async.