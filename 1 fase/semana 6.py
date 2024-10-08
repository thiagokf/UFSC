# binario --> decimal
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


# decimal --> binario
decimal = int(input())

binario = []

while decimal > 0:
    d = decimal % 2
    decimal = decimal // 2
    binario.append(d)
t = len(binario)
while t != 0:
    print(binario[t-1], end='')
    t -= 1

# # # complemento de 2 # # #
decimal = int(input())
bits = int(input())
binario = []
# for i in range(bits):
#     binario.append(0)
decimal2 = decimal
if decimal < 0:
    decimal = decimal * -1
while decimal > 0:
    d = decimal % 2
    decimal = decimal // 2
    binario.append(d)
t = len(binario)
zeros = bits - t
# for i in range(zeros):
#     del binario[i]
for i in range(t):
    binario[i], binario[t-1] = binario[t-1], binario[i]
for i in range(zeros):
    binario.insert(0, 0)

# complemento de 1
if decimal2 < 0:
    for i in range(bits):
        if binario[i] == 1:
            binario[i] = 0
        elif binario[i] == 0:
            binario[i] = 1
            
# complemento de 2
    bits -= 1
    for i in range(bits):
        if binario[bits] + 1 == 1:
            binario[bits] += 1
            break
        else:
            binario[bits] = 0
        bits -= 1

print(binario)

# Lista de Exercicio Tuplas e Listas:

# Inicialização  
lista = []
media = 0
melhor_nota = 0
menor_nota = 11

# Notas
for i in range(3):
    nota = float(input())
    lista.append(nota)
    media += nota

# Melhor e pior nota
melhor_nota = max(lista)
menor_nota = min(lista)

# Resultados
print(f"media = {media / 3:.2f}")   
print(f"melhor nota = {melhor_nota}")
print(f"menor nota = {menor_nota}")
print(f"diferença entre a maior e a menor nota = {melhor_nota - menor_nota}")



# # exercicio 2 # #

# Ler os numeros e lista
n = int(input("digite quantos numeros tera na lista: "))
lista = []

# listagem dos numeros
for i in range(n):
    numero = int(input("numero: "))
    lista.append(numero)
    
# verificar se há repetidos
print(lista)
if len(lista) != len(set(lista)): # set() elimina duplicatas na lista
    print("há valores repetidos na lista")
else:
    print("não há valores repetidos na lista")
    

# # exercicio 3 # #

tupla = (5, 12, 3, 7, 9, 21, 1, 8, 15, 4)

# pegando o maximo e o minimo
maximo = max(tupla)
minimo = min(tupla)

# posicoes do max e min
pos_max = tupla.index(maximo)
pos_min = tupla.index(minimo)

print(f"O maior numero é o {maximo} e esta na posição {pos_max}")
print(f"O menor numero é o {minimo} e esta na posição {pos_min}")


# # # exercicio 4 # # #

# pedindo os numeros e lista
n = int(input("digite quantos numeros tera na lista: "))
x = []
z = int(input("digite o numero para multiplicar os elementos da lista: "))

# listando os numeros
for i in range(n):
    numero = int(input("numero: "))
    x.append(numero)
print(x )
# multiplicacao
print(f'multiplicado por {z}: ')
p = 0
m = []
for i in range(n):
    p = x[i] * z
    m.append(p)
print(m)
    

# # # exercicio 5 # # #

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

i = 0
m = 19
while i <= m:
    u = x[m]
    p = x[i]
    del x[i]
    del x[m - 1]
    x.insert(i, u)
    x.insert(m, p)
    
    i += 1
    m -= 1

print(x)


# otimizacao do codigo (chat gpt)
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Loop até a metade da lista
for i in range(len(x) // 2):
    m = len(x) - 1 - i
    x[i], x[m] = x[m], x[i]

print(x)
