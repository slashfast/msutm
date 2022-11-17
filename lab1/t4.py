a, n = input('Введите два числа через пробел > ').split()
a = float(a)
n = int(n)
result = a

if n < 0:
    print('Исходные данные не верны!')
else:
    for i in range(1, n + 1):
        result *= a - i * n

    print(result)
