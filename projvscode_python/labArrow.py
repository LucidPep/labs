#Arrheight = 5
#Arrwidth = 10

def Arrow_Left(Arrheight, Arrwidth):
    for i in range(Arrheight):
        print()
        for j in range(Arrwidth):
            if i != 2 and (j != 2 and (j != 1 or i == 0 or i == 4)):
                print(' ', end=' ')
            else:
                print('*', end=' ')
    print()

def Arrow_Right(Arrheight, Arrwidth):
    for i in range(Arrheight):
        print()
        for j in range(Arrwidth):
            if i != 2 and (j != 7 and (j != 8 or i == 0 or i == 4)):
                print(' ', end=' ')
            else:
                print('*', end=' ')
    print()

def Arrow_Up(Arrheight, Arrwidth):
    for i in range(Arrwidth):
        print()
        for j in range(Arrheight):
            if j != 2 and (i != 2 and (i != 1 or j == 0 or j == 4)):
                print(' ', end=' ')
            else:
                print('*', end=' ')
    print()

def Arrow_Down(Arrheight, Arrwidth):
    for i in range(Arrwidth):
        print()
        for j in range(Arrheight):
            if j != 2 and (i != 7 and (i != 8 or j == 0 or j == 4)):
                print(' ', end=' ')
            else:
                print('*', end=' ')
    print()


print("Введите одну из сторон (Влево/Вправо/Вверх/Вниз): ", end='  ')
direction = input()

if direction == "Вправо":
    Arrow_Right(5, 10)
elif direction == "Влево":
    Arrow_Left(5, 10)
elif direction == "Вниз":
    Arrow_Down(5, 10)
elif direction == "Вверх":
    Arrow_Up(5, 10)
else:
    print("Неверно введенные данные!")