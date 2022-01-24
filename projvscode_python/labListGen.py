list_one = list(range(10))
print(list_one)


temp = [x*2 for x in range(10)]
print(temp)

temp_2 = [x for x in range(101) if x % 5 == 0]
print(temp_2)