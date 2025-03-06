import numpy as np
from scipy.stats import gmean

# Ввод размера матрицы с проверкой корректности
while True:
    try:
        n = int(input("Введите размерность матрицы n (положительное целое число): "))
        if n > 0:
            break
        else:
            print("Пожалуйста, введите положительное целое число.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

# Создание матрицы M с случайными числами на интервале (-3, 7)
M = np.random.uniform(low=-3, high=7, size=(n, n))

# Вывод матрицы M с округлением до сотых
print("\nМатрица M (округленная до сотых):")
for row in M:
    print(" ".join(f"{elem:.2f}" for elem in row))

# Создание вектора d из главной диагонали и его сортировка
d = np.diag(M)
d_sorted = np.sort(d)
print("\nВектор d (отсортированный по возрастанию):")
print(" ".join(f"{elem:.2f}" for elem in d_sorted))

# Вычисление среднего геометрического модулей элементов M
abs_M = np.abs(M)
geometric_mean = gmean(abs_M.flatten())
print(f"\nСреднее геометрическое модулей элементов M: {geometric_mean:.2f}")

# Создание подматрицы M2 из чётных столбцов (индексы 0, 2, 4, ...)
even_columns = [i for i in range(0, n, 2)]
M2 = M[:, even_columns]
print("\nМатрица M2 (чётные столбцы M):")
for row in M2:
    print(" ".join(f"{elem:.2f}" for elem in row))

# Создание матрицы M3 из нечётных столбцов (индексы 1, 3, 5, ...)
odd_columns = [i for i in range(1, n, 2)]
M3 = M[:, odd_columns]
print("\nМатрица M3 (нечётные столбцы M):")
for row in M3:
    print(" ".join(f"{elem:.2f}" for elem in row))
