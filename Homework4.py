# palindrome
x = input('Enter sequence to test: ')
r = x[::-1]
x_list = list(x)
r_list = list(map(str, r))
if x_list == r_list:
    print('Entered sequence is a palindrome')
else:
    print('Sequence is not a palindrome')

# lucky ticket
number = input('Enter the number: ')
numb_list = list(map(int, number))
length = len(numb_list)
mid_index = length // 2
left_p = numb_list[:mid_index]
right_p = numb_list[mid_index:]
if length % 2 == 0 and sum(left_p) == sum(right_p):
    print('Congratz, you are the lucky one!')
elif length % 2 == 0:
    print('Better luck next time')
else:
    print('You can not participate in lucky contest ')

# circle
print('Please enter coordinates of the point:')
p = list(map(int, [input('x = '), input('y = ')]))
print('Please enter coordinates of the circle center:')
c = list(map(int, [input('x = '), input('y = ')]))
r = int(input('Radius of the circle = '))
if (c[0] - p[0]) ** 2 + (c[1] - p[1]) ** 2 <= r ** 2:
    print('Point belongs to the circle')
else:
    print('Point does not belong to the circle')
