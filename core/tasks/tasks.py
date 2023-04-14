from datetime import timedelta

from celery import Celery

from config import REDIS_HOST, REDIS_PORT
from core.crud.crud import update_product

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')


@celery.task(name='update_product_task')
def update_product_task():
    update_product()


celery.conf.beat_schedule = {
    'update-product': {
        'task': 'update_product_task',
        'schedule': timedelta(seconds=10),
    },
}

celery.conf.timezone = 'Europe/Moscow'
