import numpy as np

# Ввод размера матрицы с проверкой
while True:
    try:
        n = int(input("Введите размерность матрицы n (положительное целое число): "))
        if n > 0:
            break
        else:
            print("Введите положительное число.")
    except ValueError:
        print("Некорректный ввод. Введите целое число.")

# Создание матрицы M
M = np.random.uniform(low=-7, high=7, size=(n, n))

# Вывод матрицы M с округлением
print("\nМатрица M (округленная до сотых):")
for row in M:
    print(" ".join(f"{elem:.2f}" for elem in row))

# Вектор d из главной диагонали, отсортированный
d = np.diag(M)
d_sorted = np.sort(d)
print("\nВектор d (отсортированный):")
print(" ".join(f"{elem:.2f}" for elem in d_sorted))

# Минимальный элемент во второй строке
if n >= 2:
    second_row_min = np.min(M[1, :])
    print(f"\nМинимальный элемент во второй строке: {second_row_min:.2f}")
else:
    print("\nВторая строка отсутствует, так как n < 2.")

# Сумма всех элементов
total_sum = np.sum(M)
print(f"\nСумма всех элементов матрицы M: {total_sum:.2f}")

# Матрица M2 из нечётных столбцов (индексы 1, 3, ...)
odd_columns = [i for i in range(1, n, 2)]
M2 = M[:, odd_columns]
print("\nМатрица M2 (нечётные столбцы):")
for row in M2:
    print(" ".join(f"{elem:.2f}" for elem in row))
