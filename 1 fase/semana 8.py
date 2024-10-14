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
                lista[0][m] = 225
            else:
                lista[0][m] = 0
        if verificando() != 1:
            print("*")
            
        else:
            if resposta() == 0:
                print("A")
            elif resposta() == 1:
                print("B")
            elif resposta() == 2:
                print("C")
            elif resposta() == 3:
                print("D")
            elif resposta() == 4:
                print("E")
