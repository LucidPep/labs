p = 38
for a in range(1, p):
    b = a
    k = 1
    print('-------------------------------')
    print('{0}'.format(b, k))
    while(b > 1 and k <= 17):
        b = b*a % p
        k += 1
        print('{0}'.format(b, k))