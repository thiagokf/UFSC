cadastrados = []

cad = 0
while True:
    pessoa = {}
    pessoa['nome'] = input('Digite seu nome: ')
    if pessoa['nome'] == 'fim':
        break
    cad += 1
    pessoa['idade'] = int(input('Digite sua idade: '))
    pessoa['pet'] = input('Tem pet? ')
    
    cadastrados.append(pessoa)
    
#soma das idades e tem pet
sum = 0
tem_pet = []
ntem_pet = []
for i in range(len(cadastrados)):
    id = cadastrados[i]['idade']
    sum += id
    tem = cadastrados[i]['pet']
    if tem == 'sim':
        tem_pet.append(cadastrados[i]['nome'])
    else:
        ntem_pet.append(cadastrados[i]['nome'])
           
# resultados:
print('******************************************')
print(f'{cad} pessoas foram cadastradas')
print('******************************************')
print(f'a media de idade dos cadastrados é de {sum / cad:.2f} anos')
print('******************************************')
print('os cadastrados que possuem pets são:')
for c in tem_pet:
    print(f'- {c}')

 # # # lista de exercicios # # # 
 # # exercicio 1 # #
def soma():
    som = 0
    for qt in range(qnt_compra):
            prod_compra, qntos_compra = input().split(' ')
            qntos_compra = int(qntos_compra)   
            for prod in produtos:
                if prod['produto'] == prod_compra:
                    som += prod['preco'] *  qntos_compra
    return som


qnt = int(input())
for q in range(qnt):
    qnt_prod = int(input())
    produtos = []
    for i in range(qnt_prod):
        produto, preco = input().split(' ')
        preco = float(preco)
        prod_preco = {
            'produto': produto,
            'preco': preco
        }
        produtos.append(prod_preco)
        
    qnt_compra = int(input())
    print(f"R$ {soma():.2f}")
        
# jeito de fazer soma : soma = sum(p['preco'] for p in produtos)


 # # exercicio 2 # # 
qnt_trad = int(input())
felizes_natais = []

# criando dicionario das traducoes de feliz natal
for i in range(qnt_trad):
    lingua = input()
    fn = input()
    traducoes = {
        'lingua': lingua,
        'fn': fn
    }
    felizes_natais.append(traducoes)

# nome e lingua
qnt_pessoas = int(input())
for p in range(qnt_pessoas):
    nome = input()
    lingua2 = input()
    for l in felizes_natais:
        if lingua2 == l['lingua']:
            print(nome)
            print(l['fn'])


# n = int(input())
# dict = {}
# while n:
#     n -= 1
#     lingua = input('s')
#     trad = input()
#     dict[lingua] = trad
# 
# m = int(input())
# while m:
#     m -= 1
#     pessoa = input()
#     lingua = input()
#     print(pessoa)
#     print(dict[lingua])
#     print()


number = 1
while True:
    number = int(input(""))
    if number == 0: break

    dic = {}

    for x in range(number):
        entry_a = input().split()
        dic[entry_a[0]] = entry_a[1]

    students = int(input(""))
    mis, sin = int(0), int(0)

    for x in range(students):
        count = int(0)
        name_dic = input().split()
        for y in dic[name_dic[0]]:
            if y != name_dic[1][count]:
                mis += 1
            count += 1
        if mis > 1: sin += 1

        mis = 0

    print(sin)
