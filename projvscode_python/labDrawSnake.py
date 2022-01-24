print("Введите ширину: ", end=' ')
width = input()
print("Введите длину: ", end=' ')
height = input()

for i in range(1, int(height)+1):
    print()
    for j in range(1, int(width)+1):
        print('x', end=' ') if j % 2 == 0 or (j % 2 == 1 and i % int(height) == 0 and 
        j % 4 != 1) or (i == 1 and ((j-1) % 4 == 0)) else print(' ', end=' ')