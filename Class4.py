x = [10, 20, 30, 40]
z = int(len(x))
y = x[1:z-1]
print(y)



x, y, z = int(input('x=')), int(input('y=')), int(input('z='))

if x > y and x > z:
    print(x)
elif y > z:
    print(y)
else:
    print(z)

if y < x > z:
    print(x)
elif y > z:
    print(y)
else:
    print(z)

# find if x and y are different signs
#if y * x < 0:


x = [input(), input(), input()]
print(x)
