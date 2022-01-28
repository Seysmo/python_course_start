import random

# Divider
x = list(map(int, [input('Start'), input('End')]))
div = int(input('Input divider: '))
for i in range(x[0], x[-1]+1):
    if i % div:
        continue
    else:
        print(i)


n = int(input('N'))

# i - spaces, j - *

i = 0

for j in range(n, 0, -2):
    print(i * ' ' + j * '*')
    i += 1
i -= 2
for j in range(3, n +1, 2):
    print(i * ' ' + j * '*')
    i -= 1

# fact

number = int(input('N = '))
fact = 1
while number != 1:
    fact = fact * number
    number -= 1
print(fact)

# Odd and even
x = list(map(int, (input('Enter the number: '))))
for i in x:
    if i % 2 != 0:
        x.remove(i)
print(len(x))

# append lists x2
x = int(input('List length = '))
y = [0] * x
for i in range(x):
    y[i] = random.randint(0, 1000)
print(y)
z = [0] * x
for i in range(x):
    z[i] = y[i] * 2
print(z)
for i in z:
    y.append(i)
print(y)

# wage
y = [0] * 12
for i in range(12):
    y[i] = random.randint(7500, 15000)
print(y)
print('Average wage:', sum(y) // 12)

# prime
x, y = int(input('x=')), int(input('y='))

for n in range(x, y + 1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)


# mirror list

x = input('Enter sequence to test: ')
r = x[::-1]
x = list(x)
print(x)
r = list(map(str, r))
print(r)


# Multi

x = int(input('Multi: '))

for i in range(2, 10):
    print(x, 'x', i, '=', x * i)



# Array:

x, y = int(input('List length = ')), int(input('List length = '))

z = [0] * y
for i in range(y):
    z[i] = [0] * x
for i in range(y):
    for j in range(x):
        z[i][j] = random.randint(0, 1000)
for i in range(y):
    for j in range(x):
        print(z[i][j], end='\t')
    print()