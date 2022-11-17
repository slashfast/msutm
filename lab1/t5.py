import random

y, x = '0', '0'

while y == '0' or x == '0':
    y, x = input('Введите число строк и столбцов через пробел > ').split()
    if y == '0' or x == '0':
        print('Некорректное значение!')

y = int(y)
x = int(x)
matrix = [[random.randint(-100, 100) for j in range(x)] for i in range(y)]

print('Заполненная матрица: ')

for i in matrix:
    print(' '.join(str(k).rjust(4) for k in i))

minimum = min([(y, min(enumerate(e), key=lambda t: t[1])) for y, e in enumerate(matrix)], key=lambda t: t[1])
maximum = max([(y, max(enumerate(e), key=lambda t: t[1])) for y, e in enumerate(matrix)], key=lambda t: t[1])

print(f'Минимум {minimum[1][1]}', f'Максимум {maximum[1][1]}')

matrix[minimum[0]][minimum[1][0]] = maximum[1][1]
matrix[maximum[0]][maximum[1][0]] = minimum[1][1]

print('Измененная матрица')

for i in matrix:
    print(' '.join(str(k).rjust(4) for k in i))
