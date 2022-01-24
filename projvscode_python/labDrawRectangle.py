print("Введите длину прямоугольника: ", end=' ')
R_width = input()

print("Введите ширину прямоугольника: ", end=' ')
R_height = input()

print("Если хотите сделать фигуру полой, введите Да:  ", end=' ')
hollow = input()

for i in range(int(R_width)):
    print()
    for j in range(int(R_height)):
        if (hollow.capitalize() == "Да"):
            if (i == 0 or j == 0 or i == (int(R_width)-1) or j == (int(R_height)-1)):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        else:
            print('*', end=' ')