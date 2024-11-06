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
    soma = 0
    for qt in range(qnt_compra):
        prod_compra, qntos_compra = input().split(' ')
        qntos_compra = int(qntos_compra)
        
        for prod in produtos:
            if prod['produto'] == prod_compra:
                soma += prod['preco'] *  qntos_compra
#     print(produtos)
    print(f"R$ {soma:.2f}")
        
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






while True:
    turma = []
    num_alunos = int(input())
    if num_alunos == 0:
        break
    for i in range(num_alunos):
        nome, assinatura = input().split()
        
        alunos = {
            'nome': nome,
            'assinatura': assinatura
        }
        turma.append(alunos)
    alunos_presentes = int(input())
    
    aluno1 = []
    ass_falsa = 0
    for p in range(alunos_presentes):
        nome, assinatura = input().split()
        aluno = {
            'nome': nome,
            'assinatura': assinatura
        }
        aluno1.append(aluno)
       
        c = 0
    for c in range(alunos_presentes): 
        for l in range(alunos_presentes):
            if aluno1[c]['nome'] == turma[l]['nome']:
                comp = 0
                for s in range(len(aluno1[l]['nome'])):
                    if aluno1[l]['assinatura'][s] != turma[c]['assinatura'][s]:
                        comp += 1
                        if comp >= 2:
                            ass_falsa += 1
                            break          
    print(ass_falsa)
