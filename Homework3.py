import math

# Area of Triangle
a = int(input('Enter side A: '))
b = int(input('Enter side B: '))
c = int(input('Enter side C: '))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    print('Triangle does not exist')
else:
    print('Area of Triangle =', area)

# Apartments
apt = int(input('Enter an apartment number '))
x = range(1, 144)
if apt in x:
    print('This apartment located on the floor number', int(1 + ((apt - 1) % 36) / 4),
          'and front door number:', (1 + (apt - 1) // 36))
else:
    print('There is no such apartment in this house')

# Leap Year

x = int(input('Enter the year: '))

if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print(x, 'is a Leap Year')
        else:
            print(x, 'is not a Leap Year')
    else:
        print(x, 'is a Leap Year')
else:
    print(x, 'is not a Leap Year')

# Everything else
number = int(input('Enter the number '))
if number < 0:
    print('Number is', number)
if number < 20:
    print('Number is less than 20')
if number == 0:
    print('Number is Zero')
else:
    print('Number ain\'t Zero')
if number % 2 == 0:
    print('Number is Even')
else:
    print('Number is Odd')


print('Hello')