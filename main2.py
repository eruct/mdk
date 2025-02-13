import math
x = float(input("Введите x (x должно быть больше или равно 1): "))
x1 = float(input("Введите x1 (x должно быть больше или равно 1): "))
y = float(input("Введите y: "))
sqrt1 = math.sqrt(x + 1)
sqrt2 = math.sqrt(x1 - 1)
result1 = math.sin(sqrt1) - math.sin(sqrt2)
if x < 1:
    print("Ошибка: x не может быть равен 1")
else:
    part1 = ((x + 1) / (x - 1)) ** x
    part2 = 18 * x * y ** 2
    result2 = part1 + part2
print("Результат первой формулы:", result1)
print("Результат второй формулы:", round(result2))