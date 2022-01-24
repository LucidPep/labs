from random import *
import hashlib


# Вычисление квадратичного хэша сообщения
def hash_kvadr(m1):
    h = 0
    for i in m1:
        h += ord(i) ** 2 % 1170
    return h


# Генерация большого простого числа P
def rand_P():
    while True:
        p = randint(10 ** 5, 10 ** 7)
        if p % 2 != 0 and all(p % n != 0 for n in range(3, int((p ** 0.5) + 1))):
            return p


# Генерация большого целого числа G, причём G < P
def rand_G(p):
    while True:
        g = randint(10 ** 5, 10 ** 7)
        if (g % 2 != 0) and all(g % n != 0 for n in range(3, int((g ** 0.5) + 1))) and g < p:
            return g + 1


# Генерация случайного числа Х, причём 1 < X <= (P-1)
def rand_X(p):
    while True:
        x = randint(10 ** 5, 10 ** 7)
        if (x % 2 != 0) and all(x % n != 0 for n in range(3, int((x ** 0.5) + 1))) and x < p:
            return x + 1


# Вычисление НОД
def NOD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# Проверка взаимно простых чисел
def vz(D,M):
    if NOD(D,M) == 1:
        return False
    else:
        return True


# Генератор К, такого, что К и Р-1 взаимно простые
def get_vz(p):
    k = randint(10 ** 5, 10 ** 7)
    while vz(k,p):
        k = randint(10 ** 5, 10 ** 7)
    return k



m1 = input('Введите сообщение ')
p= rand_P()
g = rand_G(p)
x = rand_X(p)

print('P = ', p, 'G = ', g)
print('X = ', x)
y = 1

# Вычисление открытого ключа
for i in range (x):
    y = y * g % p

print('Y = ', y)

k = get_vz(p)
print('K = ', k)


m = hash_kvadr(m1)

a = 1
# Вычисление а
for i in range (k):
    a = a * g % p


b = 0
# Вычисление b по расширенному алгоритму Евклида
while m != (x * a + k * b) % (p-1):
    b += 1

# Пара чисел (a, b) образает цифровую подпись S
print('S', (a,b))
a1 = 1
# Блок проверки подписи. Если А1 и А2 равны, то подпись верна
for i in range(a):
    a1 = a1 * y % p

for i in range(b):
    a1 = a1 * a % p

a2 = 1
for i in range(m):
    a2 = a2 * g % p

print('A1 = ', a1, 'A2 = ', a2)
if a1 == a2:
    print('Подпись верна')
