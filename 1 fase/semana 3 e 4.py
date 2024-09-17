# semana 3

# exercicio 1
# Escreva um programa que imprima todos os anos bissextos do século XXI.
# Lembre-se que o primeiro ano bissexto do século foi em 2004 e
#que oúltimo será em 2096 e que os anos bissextos ocorrem
#usualmente de 4 em 4 anos.

# i = 2004
# 
# while i < 2097:
#     print(i)
#     i += 4
    
    
    
# exercicio 2
# Faça um programa que imprima na tela apenas os números ímpares
# entre 1 e 50.

# i = 1
# 
# while i < 51:
#     print(i)
#     i = (i + 2)



# exercicio 3

# i = 1
# melhor_nota = 0
# while i <= 5:
#     nome = input("nome do aluno: ")
#     nota = float(input("media geral: "))
#     mensalidade = float(input("mensalidade: "))
#     
#     if melhor_nota < nota:
#         melhor_nota = nota
#         melhor_aluno = nome
#         melhor_mensalidade = mensalidade
#     mensalidade_desconto = mensalidade - (mensalidade * 0.3)
#     i += 1
#     
# print(f"Aluno com a melhor nota: {melhor_aluno}")
# print(f"Valor da mensalidade (sem desconto): R${melhor_mensalidade:.2f}")
# print(f"Valor da mensalidade com desconto: R${mensalidade_desconto}")
    


# exercicio 4
# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
# de números pares e a quantidade de números impares.

# quantidade_par = 0
# quantidade_impar = 0
# 
# i = 0
# 
# while i < 10:
#     numero = int(input())
#     
#     if numero % 2 == 0:
#         quantidade_par += 1
#     else:
#         quantidade_impar += 1
#         
#     i += 1
# 
# print(f"o numero de pares é {quantidade_par}")
# print(f"o numero de impares é {quantidade_impar}")



# exercicio 5
# Faça um programa que peça um número inteiro
# e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível
# somente por elemesmo e por 1.



# numero = int(input())
# i = 1
# div = 0
# 
# while i <= numero:
#     if numero % i == 0:
#         div = div + 1
#     i += 1
# if div == 2:
#     print("numero primo")
# else:
#     i = 1
#     while i <= numero:
#         if numero % i == 0:
#             print(i)
#         i += 1
# print("numero nao primo")

# codigo do matheus
# aux = 0
# 
# numero = int(input(''))
# 
# if numero <= 1:
#     print('não é primo')
# 
# elif numero == 2:
#     print('é primo')
# 
# else:
#     for i in range(2, numero):
#         if numero % i == 0:
#             if aux == 0:
#                 print('Não é primo')
#                 print(1)
#                 aux += 1
#             print(i)
#     if aux == 0:
#         print('É primo')
#     else:
#         print(numero)



#  exercicio 7
# 
# n = int(input("numero de pessoas: "))
# 
# i = 1
# id_turma = 0
# while i <= n:
#     idade = int(input("idade: "))
#     id_turma = id_turma + idade
#     i = i + 1
# media = id_turma / n
# 
# if media < 26:
#     print("turma jovem")
# elif media < 61:
#     print("turma adulta")
# else:
#     print("turma idosa")



# #exercicio 8
# 
# (a, b) = map(int, input().split(' '))
# 
# i = a + 1
# somai = 0
# while a < i < b:
#     print(i)
#     somai = somai + i
#     i += 1
# print("***")
# print(somai)


#exercicio 10
# i = 0
# media = 0
# melhor_nota = 0
# while i < 3:
#     aluno = input("nome: ")
#     nota = float(input("nota: "))
#     
#     if melhor_nota < nota:
#         melhor_nota = nota
#         melhor_aluno = aluno
#     i += 1
#     
# print(melhor_aluno)
# 
# if melhor_nota >= 5.75:
#     print("Aprovado pae")
# elif melhor_nota >= 2.75:
#     print("Recuperacao noob")
# else:
#     print("Reprovado lixo")

#aux = 0

#numero = int(input(''))

#if numero <= 1:
#    print('não é primo')

#elif numero == 2:
#    print('é primo')

#else:
#    for i in range(2, numero):
#        if numero % i == 0:
#            if aux == 0:
#                print('Não é primo')
#                print(1)
#                aux += 1
#            print(i)
#    if aux == 0:
#        print('É primo')
 #   else:
#        print(numero)



# exercicio tabuada

# numero = int(input())
# print(f"tabuada do {numero}:")
# for i in range (1, 11):
#     tabuada = numero * i
#     print(f"{numero} x {i} = {tabuada}")
# 
#     i += 1



# exercicio 11

# n = int(input())
# soma_num = 0
# maior_num = 0
# menor_num = 100000000
# for i in range(n):
#     num = int(input("numero: "))
#     soma_num = num + soma_num
#     if num > maior_num:
#         maior_num = num
#     if num < menor_num:
#         menor_num = num
#         
# media = (soma_num) / n
# 
# print(f"media dos numeros: {media}")
# print(f"maior numero: {maior_num}")
# print(f"menor numero: {menor_num}")



# exercicio 12

# n = int(input("numero de praias: "))
# maior_distancia = 0
# media = 0
# praia_centro = 0
# for i in range(n):
#     praia = input("praia: ")
#     distancia = int(input("distancia: "))

#     media = distancia + media

#     if maior_distancia < distancia:
#         maior_distancia = distancia
#         praia_longe = praia
    
#     if 15 < distancia < 20:
#        praia_centro += 1

# media = media / n

# print(f"praia mais distante: {praia_longe} com {maior_distancia}km de distancia do centro")
# print(f"{praia_centro} estao entre 15km e 20km de distancia do centro")
# print(f"media de distancia das praias: {media:.1f}")

        

# Semana 4

#exercicio 1

# sexo = input()

# match (sexo):
#     case "masculino":
#       print("M")
#     case "feminino":
#       print("F")
#     case _:
#       print("erro. insira novamente")


# try:
#     numero = int(input("digite um numero: "))
#     print(f"o dobro de {numero} é {numero*2}")
# except:
#     print("ERRO: Digite um numero inteiro!")

# exercicio 2
import random
n = 8
value = 0
while value != n:
    value = int(input())
    value == n
    
print(f"acertou, o numero certo é {n}")

# exercicio 3   
salario = float(input())

desconto = salario * 0.11

if desconto > 320:
    desconto = 320
    x = (32000) / salario 
else:
    desconto = desconto
    x = 11
novo_salario = salario - (desconto)

print(f"o novo salario é {novo_salario} com {x}% de desconto")   


# exercicio 1075
n = int(input())

for i in range(1, 10000):
    if i % n == 2:
        print(i)

#exercicio 1078
n = int(input())

i = 1
tabuada = 0
while i <= 10:
    tabuada = n*i
    print(f"{i} x {n} = {tabuada}")
    
    i += 1

# exercicio 1146: chat gpt altos codigo slc

while True:
        # Lê um número inteiro do usuário
    X = int(input("Digite um número inteiro (ou 0 para parar): "))
        
        # Se o número for zero, o programa deve parar
    if X == 0:
        break
        
        # Cria uma lista com a sequência de números de 1 até X
    sequencia = []
    for i in range(1, X + 1):
        sequencia.append(str(i))  # Adiciona o número como string à lista
        
        # Junta os números com espaço e imprime
    print(" ".join(sequencia))


# exercicio 1134
n = 0
gasolina = 0
alcool = 0
diesel = 0
while n != 4:
    n = int(input())
    match (n):
        case 1:
            alcool += 1
        case 2:
            gasolina += 1
        case 3:
            diesel += 1
        case 4:
            break
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")

# exercicio 1101

i = 1
soma = 0
while i != 0:
    (m, n) = map(int, input().split(' '))

    if m == 0 or n == 0:
        break
    if m > n:
        i = n
        n = n - 1
        while n != m:
            num = n + 1
            print(num, end=' ')
            soma = soma + num
            n = n + 1
        print(f"Sum={soma}")
    elif m < n:
        i = m
        m = m - 1
        while m != n:
            num = m + 1
            print(num, end=' ')
            soma = soma + num
            m = m + 1
        print(f"Sum={soma}")

    i = n
    n = n - 1
    while n != m:
        num = n + 1
        print(num, end=' ')
        soma = soma + num
        n = n + 1
    print(soma)
