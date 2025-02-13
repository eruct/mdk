n = input("Введите число: ")
f = False
for i in '0123456789':
    if n.count(i) >= 3:
        f = True
        break
print(f)