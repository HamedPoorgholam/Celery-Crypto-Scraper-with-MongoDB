
from re import X
from celery import Celery 
from celery.schedules import crontab
from datetime import timedelta
import os 
app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')


app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'crypto_info_maker',
        'schedule':6,
        'args': (['scrapy crawl crypto -o crypto_info.json'],)

    },
 }

@app.task(name='crypto_info_maker')
def crypto_info_maker(x):
   with open('crypto_info.json', 'w') as f:
     f.write('') 
   return os.system(x[0])

    


# @app.task(name='add')
# def add(x,y):
#   return x+y
# 


