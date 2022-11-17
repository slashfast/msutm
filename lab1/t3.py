from math import log10

number = abs(int(input('Введите целое число = ')))
isInside = False

for _ in range(int(log10(abs(number))) + 1 if number != 0 else 1):
    if int(number % 10 % 4) == 0:
        isInside = True
        break
    number /= 10

print('Цифра входит в запись числа' if isInside else 'Цифра НЕ входит в запись числа')
