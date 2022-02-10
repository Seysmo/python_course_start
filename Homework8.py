import string
from random import randrange

x = input('Sentence 1: ')
y = input('Sentence 2: ')
for i in string.punctuation:
    while 2 * i in x:
        x = x.replace(2 * i, i)
for j in string.punctuation:
    while 2 * j in y:
        y = y.replace(2 * j, j)
x = x.split()
y = y.split()
x = ' '.join(x)
y = ' '.join(y)
x = set(list(x))
y = set(list(y))
z = x.intersection(y)
print(z)

# lists
x = int(input('List length = '))
y = [0] * x
z = [0] * x
for i in range(x):
    y[i] = randrange(0, 100, 3)
    z[i] = randrange(0, 100, 5)
w = set(y).intersection(set(z))
print(w)
