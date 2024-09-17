#EXERCICIO 1

# funcionario = int(input())
# num_horas = int(input())
# hora = float(input())
# 
# salario = num_horas * hora
# 
# print(f"NUMBER = U${funcionario}")
# print(f"SALARY = U${salario:.2f}")



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
# precototal = i
# n=0
# while n < f:
#     d += 1
#     if d % 2 == 0:
#         precototal += x
#     if d % 2 != 0:
#         precototal -= x
#     n = n + 1
# print(precototal)

# exercicio 2600

# numero_teste = int(input())
# 
# l1 = int(input())
# (l2, l3, l4, l5) = map(int, input().split(' '))
# l6 = int(input())
# 
# if l1 + l6 == 7 and l2 + l4 == 7 and l3 + l5 == 7:
#     print("SIM")
# else:
#     print("NAO")



#exercicio 1046

# (inicio, fim) = map(int, input().split(' '))
# 
# if fim > inicio:
#     tempo_jogo = fim - inicio
# elif inicio > fim:
#     tempo_jogo = (24 - inicio) + fim
# else:
#     tempo_jogo = 24
#     
# print(f"O JOGO DUROU {tempo_jogo} HORA(S)") 
    


#exercicio 1047

# (hi, mi, hf, mf) = map(int, input().split(' '))
# 
# duracao_min = ((hf - hi) * 60) + (mf - mi)
# 
# if duracao_min <=0:
#     duracao_min = duracao_min + 24*60
# hora = duracao_min // 60
# minuto = duracao_min % 60
# 
# if hf == hi and mf == mi:
#     hora = 24
#     minuto = 0
# 
# print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
   

  
# exercicio 2375

# diametro = int(input())
# 
# (h, l, p) = map(int, input().split(' '))
# 
# if diametro > h or diametro > l or diametro > p:
#     print("N")
# else:
#     print("S")


# exercicio 1048

# salario = float(input())
# 
# 
# if salario <= 400:
#     aumento = salario + (salario * 0.15)
#     reajuste = (salario * 0.15)
#     percentual = "15 %"
# elif salario <= 800:
#     aumento = salario + (salario * 0.12)
#     reajuste = (salario * 0.12)
#     percentual = "12 %"
# elif salario <= 1200:
#     aumento = salario + (salario * 0.10)
#     reajuste = (salario * 0.10)
#     percentual = "10 %"
# elif salario <= 2000:
#     aumento = salario + (salario * 0.07)
#     reajuste = (salario * 0.07)
#     percentual = "7 %"
# else:
#     aumento = salario + (salario * 0.04)
#     reajuste = (salario * 0.04)
#     percentual = "4 %"
#     
# print(f"Novo salario: {aumento:.2f}")
# print(f"Reajuste ganho: {reajuste:.2f}")
# print(f"Em percentual: {percentual}")



# exercicio 2409
# (a, b, c) = map(int, input().split(' '))
# (h, l) = map(int, input().split(' '))
# 
# if A <= H and B <= L:
#         print('S')
#     elif A <= H and C <= L:
#         print('S')
#     elif B <= H and A <= L:
#         print('S')
#     elif B <= H and C <= L:
#         print('S')
#     elif C <= H and A <= L:
#         print('S')
#     elif C <= H and B <= L:
#         print('S')
#     else:
#         print('N')




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

