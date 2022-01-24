#Виженер

def pause():
    programPause = input("Нажмите <ENTER> для продолжения...")
    
alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alph2 = alph.upper()
print('Шифр Виженера')
m1 = input('Введите сообщение: ')
m2 = ''
k = input("Введите ключ: ")
# Составление ключевой последовательности
j = k + m1
ki = 0
for i in m1: #блок шифрования
    # С = (М + К) mod N для больших букв
    if i.isupper():
        m2 += alph2[(alph2.find(i) + alph2.find(j[ki].upper())) % len(alph2)]
    # С = (М + К) mod N для маленьких букв
    elif i.islower():
        m2 += alph[(alph.find(i) + alph.find(j[ki])) % len(alph)]
    else:
        m2 += i
    ki = (ki + 1) % len(j)
print('Зашифрованное сообщение: ', m2)


m1 = ''
ki = 0

for i in m2:
    # С = (М - К) mod N для больших букв
    if i.isupper():
        m1 += alph2[(alph2.find(i) - alph2.find(j[ki].upper())) % len(alph2)]
    # С = (М - К) mod N для маленьких букв
    elif i.islower():
        m1 += alph[(alph.find(i) - alph.find(j[ki])) % len(alph)]
    else:
        m1 += i
    ki = (ki + 1) % len(j)
    
print('Расшифрованное сообщение: ', m1)

pause()
