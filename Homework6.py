import math
import re
from wordsegment import load, segment

# Names
x = input('Name: ')
d = 0
# istitle - returns True if every word in string starts from capital letter
if x[0].isupper() is True and x[1:].islower() is True and x.isalpha() is True:
    print('Correct')
else:
    print('Double check your input')

# Count
x, c = input('Enter text: '), input('Count character: ')
print(x.count(c, 0, len(x)))

# Pi
n = 2
for i in range(2, 11):
    print('Pi =', str(round(math.pi, n)))
    n += 1
for i in range(2, 11):
    res = f'{math.pi:.{i}f}'
    print(res)

# Sum of number
x = input('Sentence: ')
z = [0] * len(x)
i = 0
for j in range(len(x)):
    z[j] = int(ord(x[i]))
    i += 1
print(z)
print(sum(z))

# Leave the longest
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
res = max(x, key=len)

# HTML clean up
CLEANR = re.compile('<.*?>')


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

with open('view-source_www.columbia.edu__fdc_sample.txt', 'r') as file:
    data = file.read()
    print(data)
    data = cleanhtml(data)
with open(r'view-source_www.columbia.edu__fdc_sample_app.txt', 'w') as file:
    file.write(data)


# text breakdown
load()
x = input('Vovochka is moron: ')
print(segment(x))
x = segment(x)
j = 0
while len(x) > 1:
    if len(x[j]) >= len(x[j + 1]):
        x.remove(x[j])
    else:
        x.remove(x[j + 1])
print(x)
n = len(x)
for i in range(len(x) // 2):
    p = x[:i]
    if len(p) * x.count(p) == n:
        print(p)
        break
    else:
        print('Wrong input')