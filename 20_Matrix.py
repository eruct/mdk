import numpy as np
import matrix_operations as mo

# Пример матриц
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Сохранение матриц
mo.save_matrices(A, B)

# Умножение
print("A × B:")
print(mo.multiply_matrices(A, B))

# Транспонирование
print("\nТранспонированная A:")
print(mo.transpose_matrix(A))

# Определитель
print("\nОпределитель A:", mo.determinant(A))

# Решение системы Ax = b
b = np.array([1, 2])
solution = mo.cramer_method(A, b)
print("\nРешение системы:", solution)

# Отображение матрицы
print("\nМатрица A:")
mo.display_matrix(A)

# Вычисление C
C = mo.compute_C(A, B)
print("\nC = A × B - B × A:")
print(C)
