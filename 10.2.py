import random

def sozdat_matritsu(n):
    chisla = random.sample(range(1, 1000), n * n)
    return [chisla[i*n : (i+1)*n] for i in range(n)]

def obrabotat_matritsu(matritsa):
    diagonal = [matritsa[i][i] for i in range(len(matritsa))]
    sled = sum(diagonal)
    preobrazovannaya = []
    for nomer_stroki, stroka in enumerate(matritsa):
        if nomer_stroki % 2 == 1:  # Четные строки (индекс 1, 3, 5...)
            novaya_stroka = [elem / sled for elem in stroka]
        else:
            novaya_stroka = list(stroka)
        preobrazovannaya.append(novaya_stroka)
    
    return diagonal, sled, preobrazovannaya

n = 3
matritsa = sozdat_matritsu(n)  # Создаем случайную матрицу
diagonal, sled, preobrazovannaya = obrabotat_matritsu(matritsa)

print("Случайная матрица:")
for stroka in matritsa:
    print(stroka)

print("\nДиагональные элементы:", diagonal)
print("След матрицы:", sled)
print("\nПреобразованная матрица:")
for stroka in preobrazovannaya:
    print([round(elem, 2) if isinstance(elem, float) else elem for elem in stroka])
