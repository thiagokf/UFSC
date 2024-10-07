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
