a = int(input("Введите общее число а: "))
n = int(input("Введите общее число n (n должно быть больше a): "))

while a >= n:
    n = int(input("Ваше число n не удовлетворяет вышеописанным условиям. Повторите попытку: "))

ka = int(input("Введите число ka (ka должно быть меньше n): "))

while ka >= n:
    ka = int(input("Ваше число ka не удовлетворяет вышеописанным условиям. Повторите попытку: "))

kb = int(input("Введите число kb (kb должно быть меньше n): "))
    
while kb >= n:
    kb = int(input("Введите число kb не удовлетворяет вышеописанным условиям. Повторите попытку: "))

Ya = a ** ka % n
print ('Ya = ', Ya)
Yb = a ** kb % n
print('Yb = ', Yb)

Za = a**(kb*ka)%n
print ('Za = ', Za)
Zb = a**(ka*kb)%n
print ('Zb = ', Zb)

K = (a**(Za*Zb))%n
print ("Ваш общий ключ: ", K)