from task1 import long_process, long_process_celery
import time

start_time = time.time()
for i in range(4):
    long_process(i,i)

end_time = time.time()
print(end_time - start_time)

res = []
for i in range(5):
    res.append(long_process_celery.delay(i, i))