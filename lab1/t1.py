import math

x = float(input('Введите x = '))
y = float(input('Введите y = '))
z = float(input('Введите z = '))

result = (x + 0.45 * z) / (7 * y) + (x * y) / (math.sin(x - 2 * z))

print(f'Результат: {result}')
