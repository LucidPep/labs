#Белазо

def pause():
    programPause = input("Нажмите <ENTER> для продолжения...")
    
alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alph2 = alph.upper()
print('Шифр Белазо')
m1 = input('Введите сообщение: ')
m2 = ''
k = input("Введите ключ: ")
ki = 0
for i in m1: #блок шифрования
    # (С = М + К) mod N для больших букв
    if i.isupper():
        m2 += alph2[(alph2.find(i) + alph2.find(k[ki].upper())) % len(alph2)]
    # (С = М + К) mod N для больших букв
    elif i.islower():
        m2 += alph[(alph.find(i) + alph.find(k[ki])) % len(alph)]
    else:
        m2 += i
    # Переход на следующий символ ключа. Модуль для того, чтобы зациклить над всем сообщением.
    ki = (ki + 1) % len(k)
print('Зашифрованное сообщение: ', m2)


m1 = ''
ki = 0
# Блок расшифровки. Всё по аналогии с шифрованием
for i in m2:
    if i.isupper():
        m1 += alph2[(alph2.find(i) - alph2.find(k[ki].upper())) % len(alph2)]
    elif i.islower():
        m1 += alph[(alph.find(i) - alph.find(k[ki])) % len(alph)]
    else:
        m1 += i
    ki = (ki + 1) % len(k)
    
print('Расшифрованное сообщение: ', m1)

pause()
