a1 = int(input())
a2 = int(input())
a3 = int(input())

andar1 = 2 * a2 + 4 * a3
andar2 = 2 * a1 + 2 * a3
andar3 = 4 * a1 + 2 * a2

menor = min(andar1, andar2, andar3)

print(menor)