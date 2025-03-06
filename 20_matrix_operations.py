import numpy as np

def save_matrices(A, B, filename='matrices.npy'):
    """Сохраняет матрицы A и B в файл."""
    np.save(filename, {'A': A, 'B': B})

def multiply_matrices(A, B):
    """Умножает матрицы A и B."""
    return np.dot(A, B)

def transpose_matrix(A):
    """Возвращает транспонированную матрицу A."""
    return np.transpose(A)

def determinant(A):
    """Вычисляет определитель матрицы A."""
    return np.linalg.det(A)

def cramer_method(A, b):
    """Решает систему Ax = b методом Крамера."""
    n = A.shape[0]
    det_A = determinant(A)
    if det_A == 0:
        return None
    x = []
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        x.append(determinant(Ai) / det_A)
    return np.array(x)

def display_matrix(A):
    """Отображает матрицу A."""
    print(A)

def compute_C(A, B):
    """Вычисляет C = A × B - B × A."""
    return multiply_matrices(A, B) - multiply_matrices(B, A)
