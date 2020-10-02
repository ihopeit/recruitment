# DJANGO_SETTINGS_MODULE=settings.local celery -A recruitment beat 
DJANGO_SETTINGS_MODULE=settings.local celery -A recruitment beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
