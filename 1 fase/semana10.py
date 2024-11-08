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


def verificacao():
    entry_a = input().split()
    nome1 = entry_a[0]
    assinatura1 = entry_a[1]
    mis = 0
    falsa = 0
    if nome1 in aluno:
        if assinatura1 != aluno[nome1]:
            count = int(0)
            for v in assinatura1:
                if v != aluno[nome1][count]:
                    mis += 1
                count += 1
            if mis >= 2:
                falsa += 1
            return falsa
        else:
            return 0
            
while True:
    lista = []
    qnt = int(input())
    if qnt == 0:
        break
    else:
        aluno = {}
        for i in range(qnt):
            entry_a = input().split()
            nome = entry_a[0]
            assinatura = entry_a[1]
            aluno[nome] = assinatura     

            lista.append(aluno)
        ass_falsa = 0
        qnt_presente = int(input())
        for n in range(qnt_presente):
            ass_falsa += verificacao()
    print(ass_falsa)


lista = [{'lingua':'brasil', 'fn':'Feliz Natal!'}, {'lingua':'alemanha', 'fn':'Frohliche Weihnachten!'}, {'lingua':'austria', 'fn':'Frohe Weihnacht!'}, {'lingua':'coreia', 'fn':'Chuk Sung Tan!'}, {'lingua':'espanha', 'fn':'Feliz Navidad!'}, {'lingua':'grecia', 'fn':'Kala Christougena!'}, {'lingua':'estados-unidos', 'fn':'Merry Christmas!'}, {'lingua':'inglaterra', 'fn':'Merry Christmas!'}, {'lingua':'australia', 'fn':'Merry Christmas!'}, {'lingua':'portugal', 'fn':'Feliz Natal!'}, {'lingua':'suecia', 'fn':'God Jul!'}, {'lingua':'turquia', 'fn':'Mutlu Noeller'}, {'lingua':'argentina', 'fn':'Feliz Navidad!'}, {'lingua':'chile', 'fn':'Feliz Navidad!'}, {'lingua':'mexico', 'fn':'Feliz Navidad!'}, {'lingua':'antardida', 'fn':'Merry Christmas!'}, {'lingua':'canada', 'fn':'Merry Christmas!'}, {'lingua':'irlanda', 'fn':'Nollaig Shona Dhuit!'}, {'lingua':'belgica', 'fn':'Zalig Kerstfeest!'}, {'lingua':'italia', 'fn':'Buon Natale!'}, {'lingua':'libia', 'fn':'Buon Natale!'}, {'lingua':'siria', 'fn':'Milad Mubarak!'}, {'lingua':'marrocos', 'fn':'Milad Mubarak!'}, {'lingua':'japao', 'fn':'Merii Kurisumasu!'}]


while True:
    try:
        pais = input()

        for x in range(len(lista) + 1):
            if x == len(lista):
                print('--- NOT FOUND ---')
            elif pais == lista[x]['lingua']:
                print(lista[x]['fn'])
                break
            
    except EOFError:
        break
