import math
z = float(input("Введите число z: "))
x = float(input("Введите число x: "))
a = float(input("Введите число a: "))
znam1 = math.pow(x, 3) + z
shisl1 = x + 1
itog1 = (shisl1 / znam1) * math.fabs(x - math.pow(a, 5))
znam2 = math.pow(x, 2/3) + z * x
shisl2 = 3 - math.pow(z, 4)
itog2 = shisl2 / znam2
b = itog1 + itog2
print(b)