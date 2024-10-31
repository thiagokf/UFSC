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
