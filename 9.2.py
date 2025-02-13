n = int(input("Введите количество точек: "))

points = []

for i in range(n):
    while True:
        user_input = input(f"Точка {i + 1} (x y): ").split()

        if len(user_input) == 2:
            try:
                x = float(user_input[0])
                y = float(user_input[1])
                points.append((x, y))
                break
            except ValueError:
                print("Ошибка: введите два числа (x и y), разделенные пробелом.")
        else:
            print("Ошибка: нужно ввести два числа (x и y), разделенные пробелом.")

max_distance_sq = -1
best_pair = (0, 0)

for i in range(n):
    for j in range(i + 1, n):
        dx, dy = points[i][0] - points[j][0], points[i][1] - points[j][1]
        distance_sq = dx ** 2 + dy ** 2
        if distance_sq > max_distance_sq:
            max_distance_sq = distance_sq
            best_pair = (i, j)

print(f"Пара с наибольшим расстоянием: {best_pair[0] + 1} и {best_pair[1] + 1}")
