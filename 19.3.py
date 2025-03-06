import numpy as np
from scipy.integrate import quad

# 1. Производная
def derivative(x):
    term1 = np.exp(x**3) * np.cos(x) + 3 * x**2 * np.exp(x**3) * np.sin(x)
    csc_x = 1 / np.sin(x)
    cot_x = np.cos(x) / np.sin(x)
    term2 = (-csc_x**3 - csc_x * cot_x**2) * (x - 1) + cot_x * csc_x
    return term1 + term2

x_val = float(input("Введите x для вычисления производной: "))
y_prime = derivative(x_val)
print(f"Производная в точке x = {x_val}: {y_prime:.2f}")

# 2. Интеграл (определённый, от a до b)
def integrand(x):
    num = np.sin(x) * x**2
    den = np.sqrt(np.cos(x) + np.sin(x**2))
    log_term = np.log(np.sin(x) / np.cos(2 * x))
    return (num / den) * log_term

a = 0.1  # Начало интервала (избегаем нуля из-за особенностей)
b = 1.0  # Конец интервала
integral, error = quad(integrand, a, b)
print(f"Интеграл от {a} до {b}: {integral:.2f} (ошибка: {error:.2e})")

# 3. Ряд
def series_sum(E):
    S = 0
    i = 0
    while True:
        term = 1 / (4**i + 5**i)
        S += term
        if term < E:
            break
        i += 1
    return S, i

E = 1e-6  # Погрешность
S_approx, iterations = series_sum(E)
print(f"Сумма ряда: {S_approx:.6f} (итераций: {iterations})")
