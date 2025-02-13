x = float(input("Введите x: "))
y = float(input("Введите y: "))
m = float(input("Введите m (меньше n): "))
n = float(input("Введите n: "))
if m >= n:
    print("Ошибка: m должно быть меньше n")
else:
    result = (y > m) and (y < n)
    print("Результат:", result)