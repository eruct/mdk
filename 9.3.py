arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

if not arr:
    print("Массив пуст!")
else:
    average = sum(arr) / len(arr)
    greater = []
    less = []

    for num in arr:
        if num > average:
            greater.append(num)
        elif num < average:
            less.append(num)

    print("Элементы больше среднего:", greater)
    print("Элементы меньше среднего:", less)