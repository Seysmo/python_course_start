def larrgestPal(n):
    high = (10 ** (n)) - 1
    low = 1 + (10 ** (n - 1))

    max_num = 0
    for i in range(high, low - 1, -1):
        for j in range(i, low - 1, -1):
            product = i * j
            if (product < max_num):
                break
            number = product
            reverse = 0
            while (n != 0):
                reverse = reverse * 10 + number % 10
                number = number // 10
            if (product == reverse and product > max_num):
                max_num = product

    return max_num

n = int(input('Number of digits: '))
print(larrgestPal(n))