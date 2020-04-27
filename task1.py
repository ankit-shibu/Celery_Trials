from celery import Celery

app = Celery('task1', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y