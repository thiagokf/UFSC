#EXERCICIO 1

#funcionario = int(input())
#num_horas = int(input())
#hora = float(input())

#salario = num_horas * hora

#print(f"NUMBER = U${funcionario}")
#print(f"SALARY = U${salario:.2f}")



#exercicio idade

#total_dias = int(input())
#anos = total_dias // 365
#meses = (total_dias % 365) // 30
#dias = (total_dias % 365) % 30

#print(f"{anos} ano (s)")
#print(f"{meses} mes (es)")
#print(f"{dias} dia (s)")



#exercicio areas

# (a, b, c) = map(float, input().split(' '))
# 
# 
# triangulo = (a * c) / 2
# circulo = (3.14159 * c * c)
# trapezio = ((a + b) * c) / 2
# quadrado = b * b
# retangulo = a * b
# 
# print(f"TRIANGULO: {triangulo:.2f}")
# print(f"CIRCULO: {circulo:.4f}")
# print(f"TRAPEZIO: {trapezio:.4F}")
# print(f"QUADRADO: {quadrado:.87f}")
# print(f"TRIANGULO: {retangulo:.36f}")



# exercicio distancia entre dois pontos

# (x1, y1) = map(float, input().split(' '))
# (x2, y2) = map(float, input().split(' '))
# 
# distancia = ((x2 - x1)*2 + (y2 - y1)2)*0.5
# 
# print(f"{distancia:.2f}")



# exercicio tempo

# tempo = int(input())

# horas = tempo // 3600
# resto = tempo % 3600
# minutos = resto // 60
# segundo = resto % 60 


#print(f"{horas}:{minutos}:{segundo}")



#exercicio 1017

#h = int(input())
#km_h = int(input())

#litros = (h * km_h) / 12

#print(f"{litros:.3f}")



#exercicio 1014

#km = int(input())
#gas = float(input())

#consumo = km / gas

#print(f"{consumo:.3f} km/l")



#exercicio 1009

#name = input()
#salario = float(input())
#vendas = float(input())

#salario_bonus = salario + (vendas * 0.15)

#print(f"TOTAL = R${salario_bonus:.2f}")



#exercicio 1016

#km = int(input())
#distancia = km * 2

#print(f"{distancia} minutos")



#exercicio 1018

#total_dinheiro = int(input())

#nota_100 = total_dinheiro // 100
#resto = total_dinheiro % 100
#nota_50 = resto // 50
#resto2 = resto % 50
#nota_20 = resto2 // 20
#resto3 = resto2 % 20
#nota_10 = resto3 // 10
#resto4 = resto3 % 10
#nota_5 = resto4 // 5
#resto5 = resto4 % 5
#nota_2 = resto5 // 2
#nota_1 = resto5 % 2

#print(total_dinheiro)
#print(f"{nota_100} nota(s) de R$ 100,00")
#print(f"{nota_50} nota(s) de R$ 50,00" )
#print(f"{nota_20} nota(s) de R$ 20,00")
#print(f"{nota_10} nota(s) de R$ 10,00")
#print(f"{nota_5} nota(s) de R$ 5,00")
#print(f"{nota_2} nota(s) de R$ 2,00")
#print(f"{nota_1} nota(s) de R$ 1,00")



#semana 2


#Escreva um programa para aprovar o empréstimo bancário para compra de uma
#casa. O programa vai perguntar o valor da casa, o salário do comprador e em
#quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela
#não pode exceder 30% do salário ou então o empréstimo será negado


# valor_casa = int(input("qual o valor da casa? "))
# salario_comprador = int(input("qual o salario do comprador? "))
# anos_casa = int(input("em quantos anos vai pagar a casa? "))
# 
# prestacao_mensal = (valor_casa / (anos_casa * 12))
# parcela_minima = salario_comprador * 0.3
# 
# if parcela_minima > prestacao_mensal:
#     print("o comprador pode comprar a casa.")
# else:
#     print("o comprador não pdoe comprar a casa.")





#Elabore um programa que calcule o valor a ser pago por um produto, seu
# programa deve perguntar o valor do produto e a condição de pagamento.
# Considere:
# a. à vista (dinheiro ou cheque) – 10% de desconto
# b. 1x no cartão – 5% de desconto
# c. 2x cartão – preço normal
# d. 3x ou mais no cartão - 20% de juros



# valor_produto = float(input("qual o valor do produto? "))
# condicao_pagamento = input("qual a condicao do pagamento? ").lower()
# 
# if condicao_pagamento == "a vista no dinheiro/cheque":
#     valor_produto1 = valor_produto * 0.9
#     
# elif condicao_pagamento == "1x no cartao":
#     valor_produto1 = valor_produto * 0.95
# 
# elif condicao_pagamento == "2x no cartao":
#     valor_produto1 = valor_produto
#     
# else:
#     valor_produto1 = valor_produto * 1.2
#     
# print(f"valor = {valor_produto1}")



#exemplos da aula
#
# temperatura = float(input("qual a temperatura? "))
# unidade_inicial = input("qual a unidade? ").upper()
# unidade_final = input("qual a unidade para conversao? ").upper()
# 
# match (unidade_inicial):
# 
#     case "C":
#         match (unidade_final):
#             case "K":
#                 print(temperatura + 273.15)
#             case "F":
#                 print(temperatura * 1.8 + 32)
#             case _:
#                 print(f"a unidade {unidade_final} nao existe")
#         
#     case "F":
#         match (unidade_final):
#             case "C":
#                 print((temperatura - 32) / 1.8 )
#             case "K":
#                 print((temperatura - 32) * 5/9 + 273.25)
#             case _:
#                 print(f"a unidade {unidade_final} nao existe")
#         
#     case "K":
#         match (unidade_final):
#             case "C":
#                 print(temperatura - 273.15)
#             case "F":
#                 print((temperatura - 273.15) * 9 / 5 + 32)
#             case _:
#                 print(f"a unidade {unidade_final} nao existe")
# 
#     case _:
#         print("unidade de temperatura incorreta")

    
    
    

# 3) Desenvolva um algoritmo que leia o peso e altura de uma pessoa, calcule seu IMC
# e mostre seu status de acordo com:
# Abaixo de 18,5 – abaixo do peso
# Entre 18.5 e 25 – peso ideal
# Entre 25 e 30 - sobrepeso
# Entre 30 e 40 - obesidade
# Acima de 40 - obesidade mórbida
# Para o cálculo do IMC, considere: IMC = peso / (altura x altura)
#
#
# altura = float(input("sua altura: "))
# peso = float(input("seu peso: "))
# 
# imc = peso / ((altura / 100) * (altura / 100))
# 
# if imc < 18.5:
#     print(f"{imc:.2f} - abaixo do peso")
# elif imc < 25:
#     print(f"{imc:.2f} - peso ideal")
# elif imc < 30:
#     print(f"{imc:.2f} - sobrepeso")
# elif imc < 40:
#     print(f"{imc:.2f} - obesidade")
# else:
#     print(f"{imc:.2f} - obesidade")




# 4) Faça um programa que leia 3 notas de um aluno, calcule sua média e mostre seu
# conceito final conforme a indicação abaixo:
# Abaixo de 5 – Reprovado
# Entre 5 e menor que 7 – Em recuperação
# Igual ou maior que 7 – Aprovado
# 
# 
# (a, b, c) = map(float, input().split(' '))
# 
# media = (a + b + c) / 3
# 
# if media < 5:
#     print(f"{media:.2f} - reprovado")
# elif media < 7:
#     print(f"{media:.2f} - em recuperação")
# else:
#     print(f"{media:.2f} - aprovado")





# exercicio 1051

salario = float(input())
if salario <= 2000:
    imposto = 0
    print("isento")
elif salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print(f"R$ {imposto:.2f}")
elif salario <= 4500:
    imposto = (salario - 3000) * 0.18 + (1000 * 0.08)
    print(f"R$ {imposto:.2f}")
elif salario > 4500:
    imposto = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print(f"R$ {imposto:.2f}")
    
    





