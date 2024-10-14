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


