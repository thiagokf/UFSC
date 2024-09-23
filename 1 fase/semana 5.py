# from time import sleep
# 
# # Função contador
# def contador(inicio, fim, passo):
#     # Ajusta o passo para ser sempre positivo
#     if passo == 0:
#         passo = 1
#     if passo < 0:
#         passo = -passo
#     
#     # Faz a contagem
#     print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
#     
#     # Caso o inicio seja menor que o fim, a contagem será crescente
#     if inicio < fim:
#         for i in range(inicio, fim + 1, passo):
#             print(i, end=" ", flush=True)
#             sleep(0.3)  # Apenas para simular uma contagem lenta
#     # Caso contrário, a contagem será decrescente
#     else:
#         for i in range(inicio, fim - 1, -passo):
#             print(i, end=" ", flush=True)
#             sleep(0.3)  # Apenas para simular uma contagem lenta
# 
#     print("Fim!\n")
# 
# 
# # Realizando as contagens
# contador(1, 10, 1)  # Contagem de 1 a 10 de 1 em 1
# contador(10, 0, 2)  # Contagem de 10 a 0 de 2 em 2

# # Contagem personalizada
# inicio = int(input("Digite o início da contagem: "))
# fim = int(input("Digite o fim da contagem: "))
# passo = int(input("Digite o passo da contagem: "))
# contador(inicio, fim, passo)

# def contador(inicio, fim, passo):
#     for i in range(inicio, fim + 1, passo):
# #     i = inicio
# #     while i <= passo:
#         print(i, end=" ")
# #         i += 1
# contador(1, 10, 1)
# print("\nfim")
# contador(0, 10, 2)
# print("\nfim")
# 
# inicio = int(input("Digite o inicio da contagem: "))
# fim = int(input("Digite o fim da contagem: "))
# passo = int(input("Digite o passo da contagem: "))
# contador(inicio, fim, passo)

# def area(largura, comprimento):
#     area = largura * comprimento
#     print(area)
# largura = float(input("largura: "))
# comprimento = float(input("comprimento: "))
# 
# area(largura, comprimento)


# exercicio 2057

# def viagem(saida, tempo, fuso):
#     tempo_viagem = saida + tempo + fuso
#     if tempo_viagem > 24:
#         tempo_viagem -= 24
#     if tempo_viagem < 0:
#         tempo_viagem += 24
#     print(tempo_viagem)
# 
# (saida, tempo, fuso) = map(int, input().split(' '))
# 
# 
# viagem(saida, tempo, fuso)

# def ultrapassando(x, z):
#     soma = 0
#     num_soma = 0
#     for i in range(x, z):
#         soma = soma + (x + 1)
#         num_soma += 1
#         
#         if soma >= z:
#             print(num_soma)
#             break
# x = int(input())
# aux = 0
# while aux != 1:
#     z = int(input())
#     if z > x:
#         aux += 1
# ultrapassando(x, z)


#exercicio 1115


# aux = 0
# while aux != 1:
#     (x, y) = map(int, input().split(' '))
#     if x == 0 or y == 0:
#         aux = 1
#         
#     if x > 0 and y > 0:
#         print("primeiro")
#     elif x < 0 and y > 0:
#         print("segundo")
#     elif x < 0 and y < 0:
#         print("terceiro")
#     elif x > 0 and y < 0:
#         print("quarto")
 
        
    
# n, c = [int(x) for x in input().split()]
# pessoas = 0
# exc = 0
# 
# while n:
#     n -= 1
#     s, e = [int(x) for x in input().split()]
#     pessoas += e
#     pessoas -= s
#     if pessoas > c:
#         exc = 1
# 
# if exc:
#     print('S')
# else:
#     print('N')
    
    
    
#(n, c) = map(int, input().split(' '))
#pessoas = 0
#exc = 0

#i = 0
#while i < n:
#    (s, e) = map(int, input().split(' '))
#    pessoas += e
#    pessoas -= s
#    if pessoas > c:
#        exc = 1
#    i += 1

#if exc == 1:
#    print("S")
#else:
#    print("N")


# com return

