a, n = input('a∈ℝ n∈ℤ = ').split()  # 1
a = float(a)  # 1
n = int(n)  # 1

if n < 0:  # 2
    print('Входные данные не верны!')  # 3
else:  # 4
    result = a  # 4
    for i in range(1, n + 1):  # 5
        result *= (a - i * n)  # 6
    print(result)  # 7
# 8
