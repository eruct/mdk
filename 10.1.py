import random

def sozdat_matritsu(n):
    chisla = random.sample(range(1, 312), n * n)

    matritsa = []
    for i in range(n):
        start = i * n
        end = start + n
        stroka = chisla[start:end]
        matritsa.append(stroka)
    
    return matritsa

n = 3
matritsa = sozdat_matritsu(n)
print("Матрица порядка", n)
for stroka in matritsa:
    print(stroka)
