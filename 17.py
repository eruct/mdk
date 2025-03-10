import numpy as np

def main():
    # Шаг 1: Ввод размера матрицы с проверкой корректности
    while True:
        try:
            n = int(input("Введите размерность матрицы n (положительное целое число): "))
            if n > 0:
                break  # Выход из цикла, если введено корректное число
            else:
                print("Пожалуйста, введите положительное целое число.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    # Шаг 2: Создание матрицы M размером n x n с случайными числами
    # Используем np.random.uniform для генерации чисел в диапазоне (-3, 7)
    M = np.random.uniform(low=-3, high=7, size=(n, n))

    # Шаг 3: Вывод матрицы M с двумя знаками после запятой
    print("\nМатрица M:")
    for row in M:
        # Форматируем каждый элемент строки до двух знаков после запятой
        print(" ".join(f"{elem:.2f}" for elem in row))

    # Шаг 4: Извлечение главной диагонали в вектор d и его вывод
    d = np.diag(M)  # Извлекаем элементы главной диагонали
    print("\nВектор d (главная диагональ):")
    print(" ".join(f"{elem:.2f}" for elem in d))  # Выводим с двумя знаками после запятой

    # Шаг 5: Создание подматрицы M2 из нечётных столбцов матрицы M
    # В Python индексы начинаются с 0, поэтому нечётные столбцы — это 1, 3, 5 и т.д.
    odd_columns = [i for i in range(1, n, 2)]  # Список индексов нечётных столбцов
    M2 = M[:, odd_columns]  # Извлекаем указанные столбцы из M

    # Вывод матрицы M2
    print("\nМатрица M2 (нечётные столбцы M):")
    for row in M2:
        print(" ".join(f"{elem:.2f}" for elem in row))

    # Шаг 6: Умножение матриц M на M2 (предполагаем, что M1 — это M)
    M1 = M  # В задаче M1 не определена, предположим, что это исходная матрица M
    # Проверяем возможность умножения: M — это n x n, M2 — это n x m, где m — число нечётных столбцов
    m = M2.shape[1]  # Количество столбцов в M2
    if n == m:  # Умножение возможно только если размеры совпадают
        result = np.dot(M1, M2)  # Выполняем умножение матриц
        print("\nРезультат умножения M1 на M2:")
        for row in result:
            print(" ".join(f"{elem:.2f}" for elem in row))
    else:
        # Если умножение невозможно, выводим сообщение
        print("\nУмножение M1 на M2 невозможно, так как количество столбцов M1 "
              f"({n}) не равно количеству строк M2 ({m}).")

# Запуск программы
if __name__ == "__main__":
    main()
