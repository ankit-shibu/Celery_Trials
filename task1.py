from celery import Celery
import time

app = Celery()

def long_process(x, y):
    time.sleep(5)
    return x+y

@app.task
def long_process_celery(x, y):
    time.sleep(5)
    return x + y