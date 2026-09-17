a, b, c = map(int, input().split())

original = [a, b, c]
ordenados = sorted(original)

for numero in ordenados:
    print(numero)

print()

for numero in original:
    print(numero) 