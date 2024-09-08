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

# salario = float(input())
# 
# if salario <= 2000:
#     imposto = 0
#     print("Isento")
# elif salario <= 3000:
#     imposto = (salario - 2000) * 0.08
#     print(f"R$ {imposto:.2f}")
# elif salario <= 4500:
#     imposto = (salario - 3000) * 0.18 + (1000 * 0.08)
#     print(f"R$ {imposto:.2f}")
# elif salario > 4500:
#     imposto = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
#     print(f"R$ {imposto:.2f}")




#tipos de triangulos
#Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente,
#de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo 
#que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

#(x, y, z) = map(float, input().split(' '))

#if (x >= y) and (x >= z):
 #   a = x
#    b = y
#    c = z
#if (y >= x) and (y >= z):
  #  a = y
 #   b = x 
#    c = z
#if (z >= x) and (z >= z):
   # a = z
  #  b = x
 #   c = y


#if a >= b + c:
#    print("NAO FORMA TRIANGULO")
#elif (a**2 == b**2 + c**2):
#    print("TRIANGULO RETANGULO")
#elif (a**2 > b**2 + c**2):
 #   print("TRIANGULO OBTUSANGULO")
#elif (a**2 < b**2 + c**2):
#    print("TRIANGULO ACUTANGULO")
#if a == b == c:
#    print("TRIANGULO EQUILATERO")
#elif a == b or b == c or a == c:
#    print("TRIANGULO ISOSCELES")



#exercicio 1061

#exercicio 1061


#codigo cola
#asd
# StrDi = input().split()
# StrHi = input().split()
# StrDf = input().split()
# StrHf = input().split()
# di,df = int(StrDi[1]),int(StrDf[1])
# hhi,mmi,ssi = int(StrHi[0]),int(StrHi[2]),int(StrHi[4])
# hhf,mmf,ssf = int(StrHf[0]),int(StrHf[2]),int(StrHf[4])
# 
# min_seg = 60
# hora_seg = 3600
# dia_seg = 86400
# 
# ini = ssi + mmi*min_seg + hhi*hora_seg + di*dia_seg
# fim = ssf + mmf*min_seg + hhf*hora_seg + df*dia_seg
# 
# if ini < fim:
#     t = fim - ini
#     W = int(t/dia_seg)
#     t = t%dia_seg
#     X = int(t/hora_seg)
#     t = t%hora_seg
#     Y = int(t/min_seg)
#     t = t%min_seg
#     Z = t
# 
# print("%d dia(s)" %W)
# print("%d hora(s)" %X)
# print("%d minuto(s)" %Y)
# print("%d segundo(s)" %Z)


#cogido incial

# dia_inicio = int(input("Dia "))
# (hh, mm, ss) = map(int, input().split(':'))
# 
# dia_fim = int(input("Dia "))
# (hh2, mm2, ss2) = map(int, input().split(':'))
# 
# dias_evento = (dia_fim - dia_inicio) 
# 
# horas_evento = (hh2 - hh)
# if (horas_evento < 0):
#     horas_evento = 24 + horas_evento
#     dias_evento = dias_evento - 1
#     
# minutos_evento = (mm2 - mm)
# if (minutos_evento < 0):
#     minutos_evento = 60 + minutos_evento
#     horas_evento = horas_evento - 1
#     
# segundos_evento = (ss2 - ss)
# if (segundos_evento < 0):
#     segundos_evento = 60 + segundos_evento
#     minutos_evento = minutos_evento - 1
# if (dias_evento <= 0):
#     dias = 0
# 
# 
# print(f"{dias_evento} dia(s)")
# print(f"{horas_evento} hora(s)")
# print(f"{minutos_evento} minuto(s)")
# print(f"{segundos_evento} segundo(s)")


#exercicio DDD
#Leia um número inteiro que representa um código de DDD para discagem interurbana. 
#Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

# ddd = int(input())
# 
# if ddd == 61:
#     print("Brasilia")
# elif ddd == 71:
#     print("Salvador")
# elif ddd == 11:
#     print("Sao Paulo")
# elif ddd == 21:
#     print("Rio de Janeiro")
# elif ddd == 32:
#     print("Juiz de Fora")
# elif ddd == 19:
#     print("Campinas")
# elif ddd == 27:
#     print("Vitoria")
# elif ddd == 31:
#     print("Belo Horizonte")
# else:
#     print("DDD nao cadastrado")



#exercicio MES
#Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, 
#deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

# mes = int(input())
# 
# match (mes):
#     case 1:
#         print("January")
#     case 2:
#         print("February")
#     case 3:
#         print("March")
#     case 4:
#         print("April")
#     case 5:
#         print("May")
#     case 6:
#         print("June")
#     case 7:
#         print("July")
#     case 8:
#         print("August")
#     case 9:
#         print("September")
#     case 10:
#         print("October")
#     case 11:
#         print("November")
#     case 12:
#         print("December")
#     case _:
#         print("isso nao é um mes")




#exercicio Formuda de Bhaskara
#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
#Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
#caso haja uma divisão por 0 ou raiz de numero negativo.

# (a, b, c) = map(float, input().split(' '))
# 
# delta = (b**2 - 4 * a * c)
# raiz1 = (-b + (delta)**0.5) / (2 * a)
# raiz2 = (-b - (delta)**0.5) / (2 * a)
# 
# if delta <= 0:
#     print("Impossivel calcular")
# else:
#     print(f"R1 = {raiz1:.5f}")
#     print(f"R2 = {raiz2:.5f}")



# exercicio Vice-Campeao

# (x, y, z) = map(int, input().split(' '))
# 
# if x < y < z or z < y < x:
#     a = y
#     b = x
#     c = z
#     
# elif y < x < z or z < x < y:
#     a = x
#     b = y
#     c = z
# elif y < z < x or x < z < y:
#     a = z
#     b = y
#     c = x
# 
# print(a)



#A entrada é descrita em uma única linha, que contém seis inteiros,
#separados por um espaço em branco: Cv, Ce, Cs, Fv, Fe e Fs, (0 ≤ Cv, Ce, Fv, Fe ≤ 100),
#(-1000 ≤ Cs, Fs ≤ 1000) que são, respectivamente, o número de vitórias do Cormengo,
#o número de empates do Cormengo, o saldo de gols do Cormengo, o número de vitórias do Flaminthians,
#o número de empates do Flaminthians e o saldo de gols do Flaminthians.

# (Cv, Ce, Cs, Fv, Fe, Fs) = map(int, input().split(' '))
# 
# pontos_vitoria_C = Cv * 3
# pontos_vitoria_F = Fv * 3
# 
# pontos_C = pontos_vitoria_C + Ce
# pontos_F = pontos_vitoria_F + Fe
# 
# if pontos_C > pontos_F:
#     print("C")
# elif pontos_C < pontos_F:
#     print("F")
# elif pontos_C == pontos_F:
#     if Cs > Fs:
#         print("C")
#     elif Cs < Fs:
#         print("F")
#     else:
#         print("=")



#exercicio 2568

# (d, i, x, f) = map(int, input().split(' '))
# 
# dias = d + f
# 
# if (dias % 2 == 0):
#     preco = i + 
# else:
#     preco = i - x
#     
# print(preco)
# 
# x * (

dreg, prei, vprea, ndfut = map(int,input().split())

i=0
precototal = prei
while i < ndfut:
    dreg += 1
    if dreg % 2 == 0:
        precototal += vprea
    if dreg % 2 != 0:
        precototal -= vprea
    i += 1
print(precototal)
    




