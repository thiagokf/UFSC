binario = input()
total = len(binario)

lista = []

for i in range(total):
    lista.append(binario[i])
    
decimal = 0
n = 1
for i in range(total):
    lista_num = int(lista[i])
    decimal = decimal + (lista_num * (2** (total - n)))
    i += 1
    n += 1
print(decimal)

