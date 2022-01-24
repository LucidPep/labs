def pause():
    programPause = input("Нажмите <ENTER> для продолжения...")

# Алфавит в нижнем регистре
alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# Алфавит в верхнем регистре
alph2 = alph.upper()

m1 = input('Введите открытый текст: ')
m2 = ''
k = 0
for i in m1: #блок шифрования
    if i.isupper():
        # L = (m + k) mod N для больших букв
        m2 += alph2[(alph2.find(i) + k) % len(alph2)]
    elif i.islower():
        # L = (m + k) mod N для маленьких букв
        m2 += alph[(alph.find(i) + k) % len(alph)]
    else:
        m2 += i
    k += 1

print('Зашифрованный текст:', m2)

m1 = ''
k = 0

for i in m2:#блок расшифрования
    if i.isupper():
        # L = (m - k) mod N для больших букв
        m1 += alph2[(alph2.find(i) - k) % len(alph2)]
    elif i.islower():
        # L = (m - k) mod N для маленьких букв
        m1 += alph[(alph.find(i) - k) % len(alph)]
    else:
        m1 += i
    k += 1
    
print('Расшифрованный текст:', m1)

pause()