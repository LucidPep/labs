import random

print(random.random())
print(random.randint(0, 1000))
print(random.randrange(100, 1000, 100))

numbers = list(range(10))
random.shuffle(numbers)
print(numbers)
print(*random.choices("рандомная строка", k=3))
print(random.choices(list(range(10)), k=30))

#генерация пароля
def PasswordGen(l):
    mainstr = "1234567890-_!?&abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(''.join(random.choice(mainstr) for i in range(l)))

PasswordGen(12)

