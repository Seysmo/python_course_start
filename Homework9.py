# palindrome
def larrgestPal(n):
    high = (10 ** (n)) - 1
    low = 1 + (10 ** (n - 1))

    list_pali = []
    for i in range(low - 1, high):
        for j in range(low - 1, high):
            if str(i*j) == str(i*j)[::-1]:
                list_pali.append(int(i*j))
    return max(list_pali)

n = int(input('Number of digits: '))
print(larrgestPal(n))

# Progressions
def arprog(a, b, c):
    d = b - a
    nextn = a + c * d
    return nextn

x = list(map(int, input('x = ').split()))
print(x)
print('Next element of the progression is', arprog(a=x[0], b=x[1], c=len(x)))