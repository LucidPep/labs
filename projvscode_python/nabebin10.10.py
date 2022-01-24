p = 38
for a in range(1, p):
    b = a
    k = 1
    while(b != 1 and k <= p):
        b = (b*a)%p
        k += 1
        print(a) if b == 1 and k == p-1 else print("", end='')