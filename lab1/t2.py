import math

number = int(input('Введите целое число = '))

# Округленный в меньшую сторону десятичный логарифм числа
# всегда равен его числу знаков - 1
digits = 1 if number == 0 else int(math.log10(number)) + 1

if number % 2 == 0 and digits == 2:
    print('Число является четным двухзначным')
else:
    print('Число НЕ является четным двухзначным')
