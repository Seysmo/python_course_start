import math

x = '123'
x = int(x)
print(type(x), x)
x = float(x)
print(type(x), x)
x = int(12.345)
print(type(x), x)

# last digits of a credit card
while True:
    card = input('Input your credit card number (16 digits, no spaces): ')
    card = card.replace(' ', '')
    if len(card) == 16:
        print('Last four digits of your credit card are', card[12:16])
        break
    else:
        print('Invalid card number')

# Heron's formula calculating area of triangle
a = int(input('Enter side A: '))
b = int(input('Enter side B: '))
c = int(input('Enter side C: '))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print('Area of Triangle =', area)

# sum in 3 digits number
g = input('Enter 3 digits number:')
t = int(g[0]) + int(g[1]) + int(g[2])
print('Sum of the digits is', t)

# determine length of the number
x = input('Enter the number: ')
print('You have entered:', x)
y = len(x)
print('Length of the entered number is', y, 'digits')

# put the entered number in reverse order
reverse = x[::-1]
reverse_list = list(reverse)
print(reverse_list)

# Sum of digits in any number
z = list(x)
numbers = map(int, z)
w = list(numbers)
total = sum(w)
print('Sum of all digits is:', total)
