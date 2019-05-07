import random


def randNum():
    x = [10]
    for i in range(0, 10, 1):
        x[i] = random.random()
        return x


y = randNum()
for i in range(0, len(y)):
    print(y[i])
