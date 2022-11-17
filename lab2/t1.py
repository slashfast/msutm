from math import log10

number = int(input('Введите целое число > '))  # 1

if number % 2 == 0 and int(log10(number)) + 1 == 4:  # 2 and 4
    print('Число является четным четырехзначным')  # 5
else:  # 3
    print('Число НЕ является четным четырехзначным')  # 3, 4
# 6
