import numpy as np

def evaluate_polynomial(coeffs, x):
    """Вычисляет значение многочлена в точке x."""
    result = sum(coeffs[k] * (x ** k) for k in range(len(coeffs)))
    return result

# Пример ввода
coeffs = [1, 2, 3]  # P(x) = 1 + 2x + 3x^2
c = float(input("Введите вещественную часть c: "))
d = float(input("Введите мнимую часть d: "))
x = complex(c, d)    # x = c + i*d

# Вычисление
value = evaluate_polynomial(coeffs, x)
print(f"Значение многочлена P({x}) = {value}")
