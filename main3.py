
a = float(input("Введите объем в байтах: "))
kb = a / 1024
mb = kb / 1024
gb = mb / 1024
tb = gb / 1024
print("Килобайты:", round(kb, 1))
print("Мегабайты:", round(mb, 1))
print("Гигабайты:", round(gb, 1))
print("Терабайты:", round(tb, 1))