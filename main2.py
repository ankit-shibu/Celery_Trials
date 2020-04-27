from task2 import add
res = []
for i in range(4):
    res.append(add.delay(i, i))
    print(res[i].ready()) #Task finished processing or not
