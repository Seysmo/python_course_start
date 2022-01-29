import math

x = input('Name: ')
d = 0
if x[0].isupper() is True and x[1:].islower() is True and x.isalpha() is True:
    print('Correct')
else:
    print('Double check your input')


x, c = input('Enter text: '), input('Count character: ')
print(x.count(c, 0, len(x)))


n = 2
for i in range(2, 11):
    print('Pi =', str(round(math.pi, n)))
    n += 1


x = input('Sentence: ')
z = [0] * len(x)
i = 0
for j in range(len(x)):
    z[j] = int(ord(x[i]))
    i += 1
print(z)
print(sum(z))


x = input('Sentence: ')
while '  ' in x:
    x.replace('  ', ' ')
x = x.split(' ')
print(x)
j = 0
while len(x) > 1:
    if len(x[j]) <= len(x[j + 1]):
        x.remove(x[j])
    else:
        x.remove(x[j + 1])
print(x)



