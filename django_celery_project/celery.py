from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.from celery import Celery
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')
#celery Beat 
app.conf.beat_schedule = {
    'send-mail-every-day': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(minute='*'),
        #'args': (2,)
    }
}




# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')