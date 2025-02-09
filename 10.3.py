import random
def generirovat_pole(rows, cols, simvoly, veroyatnost_pustoy=0.3):
    pole = []
    for i in range(rows):
        stroka = []
        for i in range(cols):
            if random.random() < veroyatnost_pustoy:
                stroka.append('.')
            else:
                stroka.append(random.choice(simvoly))
        pole.append(stroka)
    return pole

def podschet_pryamougolnikov(pole):
    #Считает количество прямоугольников каждого типа на поле.
    rows = len(pole)
    if rows == 0:
        return {}
    cols = len(pole[0])
    posescheno = [[False for i in range(cols)] for i in range(rows)]
    schetchik = {}
    
    for i in range(rows):
        for j in range(cols):
            if not posescheno[i][j] and pole[i][j] != '.':
                simvol = pole[i][j]
                # Определяем границы прямоугольника
                r = i
                while r < rows and pole[r][j] == simvol and not posescheno[r][j]:
                    r += 1
                r_end = r - 1
                
                c = j
                while c < cols and pole[i][c] == simvol and not posescheno[i][c]:
                    c += 1
                c_end = c - 1
                
                # Проверка на прямоугольник
                is_rectangle = True
                for x in range(i, r_end + 1):
                    for y in range(j, c_end + 1):
                        if pole[x][y] != simvol or posescheno[x][y]:
                            is_rectangle = False
                            break
                    if not is_rectangle:
                        break
                
                if is_rectangle:
                    for x in range(i, r_end + 1):
                        for y in range(j, c_end + 1):
                            posescheno[x][y] = True
                    schetchik[simvol] = schetchik.get(simvol, 0) + 1
    return schetchik

simvoly = ['#', '?', '+', '=', '@', '$', '%']  # Символы для заполнения
rows, cols = 4, 5                              # Размер поля
pole = generirovat_pole(rows, cols, simvoly)    # Генерация поля

print("Сгенерированное поле:")
for stroka in pole:
    print(stroka)

result = podschet_pryamougolnikov(pole)
print("\nРезультат:")
for simvol, count in result.items():
    print(f"{simvol} прямоугольников – {count}")
