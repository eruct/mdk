n = list(input("Введите числа: "))
n = [int(c) for c in n if c.isdigit()]
n = [x for x in n if not x == 1]

print(n)
