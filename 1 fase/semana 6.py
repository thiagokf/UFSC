# # binario --> decimal
# binario = input()
# total = len(binario)
# 
# lista = []
# 
# for i in range(total):
#     lista.append(binario[i])
#     
# decimal = 0
# n = 1
# for i in range(total):
#     lista_num = int(lista[i])
#     decimal = decimal + (lista_num * (2** (total - n)))
#     i += 1
#     n += 1
# print(decimal)
# 
# 
# # decimal --> binario
# decimal = int(input())
# 
# binario = []
# 
# while decimal > 0:
#     d = decimal % 2
#     decimal = decimal // 2
#     binario.append(d)
# t = len(binario)
# while t != 0:
#     print(binario[t-1], end='')
#     t -= 1
# 
# 
# # Lista de Exercicio Tuplas e Listas:
# 
# # Inicialização  
# lista = []
# media = 0
# melhor_nota = 0
# menor_nota = 11
# 
# # Notas
# for i in range(3):
#     nota = float(input())
#     lista.append(nota)
#     media += nota
# 
# # Melhor e pior nota
# melhor_nota = max(lista)
# menor_nota = min(lista)
# 
# # Resultados
# print(f"media = {media / 3:.2f}")   
# print(f"melhor nota = {melhor_nota}")
# print(f"menor nota = {menor_nota}")
# print(f"diferença entre a maior e a menor nota = {melhor_nota - menor_nota}")



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
    