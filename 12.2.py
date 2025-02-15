def uniq(text):
    while True:
        vvod = input("Введите согласные буквы: ").lower()
        if vvod.isalpha():
            soglasnye = set(vvod)
            break
        else:
            print("Ошибка: введите только буквы.")

    slova = text.lower().split()

    shetsogl = {}

    for slovo in slova:
        unik = set()
        for bukva in slovo:
            if bukva in soglasnye:
                unik.add(bukva)

        for soglasnaya in unik:
            if soglasnaya in shetsogl:
                shetsogl[soglasnaya] += 1
            else:
                shetsogl[soglasnaya] = 1

    unikalnye_soglasnye = [soglasnaya for soglasnaya, schet in shetsogl.items() if schet == 1]

    unikalnye_soglasnye.sort()
    print("Согласные буквы, входящие только в одно слово:")
    for soglasnaya in unikalnye_soglasnye:
        print(soglasnaya)

text = "Это пример текста для проверки задачи"
uniq(text)
