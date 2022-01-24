func = lambda x, y: x + y
print(func(1, 5))

numbers = tuple(range(10))
numbers_new = tuple(filter(lambda x: x % 2 == 0, numbers))
print(numbers_new)

numbers_new = tuple(map(lambda x: x * 10, numbers))
print(numbers_new)