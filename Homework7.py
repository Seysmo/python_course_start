week = {0: 'Sun', 1: 'Mon', 2: 'Tues', 3: 'Thur', 4: 'Fri', 5: 'Sat', 6: ''}

day = int(input('day = '))
print(week.get(day, 'Wrong data'))


cat = { 'name' : 'Tom',
        'age' : 4,
        'name' : 'Jerry',
        'age' : 2

}

lst = '\n'.join([f'{key}.{value}' for key, value in cat.items()])

print(lst)

# Latin into int
x = input('Latin = ')
num = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
number = 0
x = x.replace("IV", "IIII")
x = x.replace("IX", "VIIII")
x = x.replace("XL", "XXXX")
x = x.replace("XC", "LXXXX")
x = x.replace("CD", "CCCC")
x = x.replace("CM", "DCCCC")
for i in x:
    number += num[i]
print(number)


