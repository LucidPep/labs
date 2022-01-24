def show_name():
    print("Герасим")

def get_name():
    return "Порфирий"

def do_nothing():
    return None

def get_name_2(k):
    return ('Введенное имя:  ' + k)

print(get_name_2(input()))

def sum(a, b = 13, c = 10):
    return a + b + c

print(sum(2))

def show_anything(a, b, *args):
    x = 0
    for arg in args:
        x += (arg + a + b)
    return x

print(show_anything(2, 3, 3, 4, 5, 1, 3))

