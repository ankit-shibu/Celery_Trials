from celery import Celery

app = Celery(backend='rpc://') #defualt takes the module name and the broker as amqp://guest:**@127.0.0.1:5672// (RabbitMQ server) 

# Definition of a task needs the decoration below
@app.task
def add(x, y):
    return x + y