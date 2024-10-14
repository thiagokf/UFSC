# # # exercicio 1 # # #
lista = []
lista_par = []
for i in range(5):
    n = int(input("digite um numero para a lista: "))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    
    
qnt9 = lista.count(9)
if 3 in lista:
    onde3 = lista.index(3)
else:
    onde3 = None

print(f"o numero 9 aparece {qnt9} vezes na lista")
if onde3:
    print(f"o numero 3 aparece na posição {onde3} da lista")
else:
    print(f"o numero 3 nao aparece na lista")
print(f"a lista contem os numero pares: {lista_par}")


# # # exercicio 2 # # #
lista = []

for i in range(5):
    n = int(input())
    lista.append(n)
print(lista)    
print(f"maior numero: {max(lista)}", end=' ')
print(f"menor numero: {min(lista)}")


# # # exercicio 3 # # #
lista = []

n = int(input("digite a quantidade de numeros para a lista: "))

for i in range(n):
    numero = int(input("numero: "))
    lista.append(numero)

print(lista)
if len(lista) != len(set(lista)):
    print("há numeros repetidos na lista")
else:
    print("não há numeros repetidos na lista")


# # # exercicio 4 # # #
n = int(input())
lista = []
for i in range(n):
    mais_perto = 0
    aux = 1000000
    (alunos, numero) = map(int, input().split(' '))
    lista = [int(x) for x in input().strip().split(' ')]
    for i in range(alunos):
        verificando = (numero - lista[i])
        if verificando < 0:
            verificando = verificando * -1
        if verificando < aux:
            aux = verificando
            mais_perto = lista[i]
    resposta = lista.index(mais_perto)
    print(resposta + 1)


# # # exercicio 5 # # #
def verificar(i):
    if i == 4:
        print('Y')
    else:
        return False
conector1 = [int(x) for x in input().strip().split(' ')]
conector2 = [int(x) for x in input().strip().split(' ')]
if True:
    for i in range(5):
        if conector1[i] == conector2[i]:
            print('N')
            break
        else:
            verificar(i)


# # # exercicio 5 # # #
X = []

# colocando itens na lista
for i in range(10):
    n = int(input())
    if n <= 0:
        X.append(1)
    else:
        X.append(n)
    print(f"X[{i}] = {X[i]}")


# # # exercicio 6 # # # 
tabuleiro = []
n = int(input())
n_bombas = 0
for i in range(n):
    bomba = int(input())
    tabuleiro.append(bomba)
# quem CARALHOS joga campo minado com UMA CASA
if n == 1:
    if bomba == 1:
        print("1")
    elif bomba == 0:
        print("0")
# fazendo o jogo para pessoas normais
else:
    for i in range(1):
        if tabuleiro[i] == 1:
            n_bombas += 1
        if tabuleiro[i+1] == 1:
            n_bombas += 1
        else:
            n_bombas = n_bombas
        print(n_bombas)
    for i in range(1, n):
        n_bombas = 0
        if i+1 >= n:
            if tabuleiro[i] == 1:
                n_bombas += 1
            if tabuleiro[i-1] == 1:
                n_bombas += 1
        else:
            if tabuleiro[i] == 1:
                n_bombas += 1
            if tabuleiro[i+1] == 1:
                n_bombas += 1
            if tabuleiro[i-1] == 1:
                n_bombas += 1  
        print(n_bombas)