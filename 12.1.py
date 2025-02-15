def a(m, t):
    count = m.intersection(t)
    return len(count)
m = {1, 2, 3, 4, 5, 5, 5, 9}
t = {4, 5, 6, 7, 5, 5, 3, 8, 9}
count = a(m, t)
print(f"Количество совпадающих членов: {count}")
