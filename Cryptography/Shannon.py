from random import getrandbits
import re

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


m1 = input('Введите сообщение:   ')
m1_bin = text_to_bits(m1)
print(m1)
print('Сообщение:    ', m1_bin)

key = bin(getrandbits(len(m1_bin)))[2:].zfill(len(m1_bin))
print('Ключ:         ', key, '\n\n\n')

m2 = ''
iterator = 0
for i in m1_bin:
    c = int(i) ^ int(key[iterator])
    m2 += str(c)
    iterator += 1

print('Зашифрованное сообщение: ', m2)

m3 = ''
iterator = 0
for k in m2:
    M = int(k) ^ int(key[iterator])
    m3 += str(M)
    iterator += 1

print('Расшифрованное сообщение: ', text_from_bits(m3))