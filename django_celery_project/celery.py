from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')

app.config_from_object('django.conf:settings', namespace='CELERY')


#celery Beat 
# app.config.beat_schedule = {

# }



# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')