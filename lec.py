stroka = "При:вет!"
index = stroka.find(':')
if stroka != index:
    a = len(stroka[:index])
else:
    a = 0
print(a)