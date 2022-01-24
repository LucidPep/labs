alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

print("Алфавит: ", end=' ')
for sign in alphabet:
    print(sign, end=' ')

print("\nАлфавит в обратном порядке: ", end=' ')
for sign in reversed(alphabet):
    print(sign, end=' ')