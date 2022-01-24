s = "rAndOm strIng"

print(s * 3)
print(len(s))

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.center(30, '_'))
print(s.ljust(30, '_'),'\n', s.rjust(30, '_'))
print(s.zfill(30))
print(s.split(' '))
print(s.replace(' ', '___'))
print(s.count(' '))
print(s.capitalize().startswith('Random'))
print('string' in s)
print('string' not in s)

print(s[0])
print(s[0:7])
print(s[-2])
print(s[2:-2:2])

