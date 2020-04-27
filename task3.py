from celery import Celery

app = Celery() 

app.config_from_object('celeryconfig') #sets up the configuration from a external module

# Definition of a task needs the decoration below
@app.task
def add(x, y):
    return x + y