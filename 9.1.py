arr = input("Введите элементы массива через пробел: ").split()

result = []
current = 1
while current < len(arr):
    result.append(str(arr[current]))
    current *= 2
print("Элементы с индексами-степенями двойки:", result)
