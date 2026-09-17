mensagem = input()
crib = input()

contador = 0

for i in range(len(mensagem) - len(crib) + 1):
    possivel = True

    for j in range(len(crib)):
        if mensagem[i + j] == crib[j]:
            possivel = False
            break

    if possivel:
        contador += 1

print(contador)