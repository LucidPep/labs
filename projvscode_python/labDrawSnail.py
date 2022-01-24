print("Введите размерность улитки: ")
dimension = input()

key = {True: 'x', False: ' '}
olist = list(range(int(dimension) // 2))

for ykey in (1, -1):
    for y in olist[::ykey]:
        slist = []
        for xkey in (1, -1):
            for x in olist[::xkey]:
                d = -2 if (xkey, ykey) == (-1, 1) else 0
                slist.append(key[x >= y+d and not y % 2 or x < y+d and not x % 2])
        
        print(' '.join(slist))