# # # Lista composta # # #

 # # exercicio 1 # #
aux = 0
i = 1
lista = []
cadastros = []
cad = 0
def cadastro():
    nome = input("nome: ")
    idade = int(input("idade: "))
    peso = float(input("peso: "))
    
    cadastros.append([nome, idade, peso])

while i != aux:
    cadastro()
    cad += 1
    con = input("Deseja continuar cadastrando? ").upper()
    if con == 'N':
        aux = 1
print(f"numero de cadastros: {cad} cadastros")

#peso
pesos = [pessoa[2] for pessoa in cadastros]
peso_max = max(pesos)
maior_peso = [pessoa for pessoa in cadastros if pessoa[2] == peso_max]
print("mais pesado:")
for pessoa in maior_peso:
    print(f"- {pessoa[0]} Idade: {pessoa[1]} Peso: {pessoa[2]} kg")

peso_min = min(pesos)
menor_peso = [pessoa for pessoa in cadastros if pessoa[2] == peso_min]
print("mais leve:")
for pessoa in menor_peso:
    print(f"- {pessoa[0]} Idade: {pessoa[1]} Peso: {pessoa[2]} kg")
    
#idade
maior20 = [pessoa for pessoa in cadastros if pessoa[1] > 20]
print("maiores de 20:")
for pessoa in maior20:
    print(f"- {pessoa[0]} (Idade: {pessoa[1]} anos)")


 # # exercicio 2 # #
tamanho = int(input("tamanho da matriz: "))
l = int(input())
c = input().upper()

op = 0
matriz = []
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)
print(matriz)


for i in range(tamanho):
    op += matriz[l][i]
if c == 'M':
    op = op / tamanho
print(op)


 # # exercicio 3 # #
tamanho = int(input("tamanho da matriz: "))
a = input().upper()
op = 0
matriz = []
for l in range(tamanho):
    linha = []
    for c in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)
for linha in matriz:
    print(linha)

for i in range(tamanho):
    for j in range(i):  
        op += matriz[i][j]
        
if a == 'M':
    op = op / tamanho
print(op)



# # # exercicio 4 # # # 
conta0 = 0
def resposta():
    
    for t in range(5):
        if lista[0][t] == 0:
            return t
def verificando():
    conta0 = 0
    for c in range(5):
        if lista[0][c] == 0:
            conta0 += 1
    return conta0

i = 0
while i != 1:
    n = int(input())
    if n == 0:
        break
    
    for i in range(n):
        lista = []
        (a,b,c,d,e) = map(int, input().split(' '))
        lista.append([a, b, c, d, e])
        
        for m in range(5):
            if lista[0][m] > 127:
                lista[0][m] = 255
            else:
                lista[0][m] = 0
        if verificando() != 1:
            print("*")
           
        else:
            r = resposta()
            if r == 0:
                print("A")
            elif r == 1:
                print("B")
            elif r == 2:
                print("C")
            elif r == 3:
                print("D")
            elif r == 4:
                print("E")

# # # lista 2 # # #

 # # exercicio 1 # #
n = int(input())
votos = [int(x) for x in input().strip().split(' ')]

satisfatorio = n - sum(votos)

if satisfatorio > n/2:
    print("Y")
else:
    print("N")


 # # exercicio 2 # #
n = int(input())

for i in range(n):
    lista = []
    numero = int(input())
    for p in range(1, numero):
        div = numero % p
        if div == 0:
            lista.append(p)
    if sum(lista) == numero:
        print(f"{numero} eh perfeito")
    else:
        print(f"{numero} nao eh perfeito")


 # # exercicio 3 # #
import copy
while True:
    lista = []
    n = int(input())
    if n == 0:
        break
    lista = [int(x) for x in input().strip().split(' ')]
    lista_nova = copy.deepcopy(lista)
    lista_nova.sort()
#     print(lista_nova)
    numero_achado = lista_nova[-2]
#     print(numero_achado)
    index = lista.index(numero_achado)
#     print(lista)
#     print(index)
    print(index + 1)



 # # exercicio 4 # # 
# definindo as contagens
m2 = 0
m3 = 0
m4 = 0
m5 = 0

# inputs
n = int(input())

lista = [int(x) for x in input().strip().split(' ')]

# tirar os numeros nao desejados por n (inutil vtnc beecronwd)
if len(lista) > n:
    while len(lista) != n:      
        del lista[n]
# definir os multiplos
else:
    for i in range(n):
        if lista[i] % 2 == 0:
            m2 += 1
        if lista[i] % 3 == 0:
            m3 +=1
        if lista[i] % 5 == 0:
            m5 +=1
        if lista[i] % 4 == 0:
            m4 +=1

# resultados
print(lista)    
print(f"{m2} Multiplo(s) de 2")
print(f"{m3} Multiplo(s) de 3")
print(f"{m4} Multiplo(s) de 4")
print(f"{m5} Multiplo(s) de 5")



 # # exercicio 5 # #
tamanho = int(input())
matriz = []
diag_prin = []
matriz_par = []
diag_sec = []
triangulo = []
ultima_coluna = []
# montando a matriz
for l in range(tamanho):
    linha = []
    for c in range(tamanho):
        elemento = int(input(f"({l})({c}): "))
        linha.append(elemento)
        # diagonal principal
        if c == l:
            diag_prin.append(elemento)
        # elemento par
        if elemento % 2 == 0:
            matriz_par.append(elemento)
    matriz.append(linha)

#diagonal secundaria
tamanho1 = tamanho
for i in range(tamanho1):
    diag_sec.append(matriz[i][tamanho1-1])
    tamanho1 -= 1
# acima da diagonal principal
p = 1
t = 0
tamanho2 = tamanho
while t != tamanho2 - 1:
    triangulo.append(matriz[t][p])
    p += 1
    if p == tamanho2:
        t += 1
        p -= 1
        
# soma ultima coluna
for k in range(tamanho):
    ultima_coluna.append(matriz[k][tamanho-1])

# resultados
print("Matriz")
for linha in matriz:
    print(linha)

# a) Mostre a soma de todos os elementos pares da matriz
print("a)")
print(matriz_par)
print(f"soma = {sum(matriz_par)}")
#  b) Mostre a média dos elementos da diagonal principal
print("b)")
print("diagonal princial")
print(diag_prin)
print(f"media = {sum(diag_prin)/len(diag_prin)}")
# c) Mostre o produto dos elementos da diagonal secundária
print("c)")
print(diag_sec)
# d) Mostre a média dos elementos acima da diagonal principal
print("d)")
print(triangulo)
print(f"media = {sum(triangulo)/len(triangulo)}")
# e) Mostre a soma dos elementos da última coluna da matriz
print("e)")
print(ultima_coluna)
print(f"soma: {sum(ultima_coluna)}")
# f) Mostre o menor valor da primeira linha da matriz

print("f)")
linha1 = matriz[0]
print(f"menor valor da primeira linha: {min(linha1)}")



 # # exercicio 6 # #
import random
print("--------------------------------")
print("       JOGA NA MEGA SENA")
print("--------------------------------")
n = int(input('Quantos jogos voce quer que eu sorteie? '))
print(f"-=-=-= SORTEANDO {n} JOGOS -=-=-=")

jogos = []
for i in range(n):
    jogo = []
    for p in range(6):
        a = random.randint(1,60)
        jogo.append(a)
    jogos.append(jogo)
c = 1
for jogo in jogos:
    print(f"Jogo {c}: {jogo}")
    c += 1
print("-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=")



 # # exercicio 7 # #
n = int(input("numero de alunos: "))
turma = []
for i in range(n):
    nota = []
    aluno = []
    nome = input("nome: ").lower()
    nota = [int(x) for x in input("notas: ").strip().split(' ')]
    media = sum(nota)/ 3
    
    aluno.append(nome)
    aluno.append(nota)
    aluno.append(media)
    
    turma.append(aluno)

chamada = input("qual aluno quer chamar? ")
for c in range(n):
    if turma[c][0] == chamada:
        print(turma[c])
        
    elif c == n -1:
        print("esse aluno não foi cadastrado")

