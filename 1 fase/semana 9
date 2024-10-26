matriculados = []

um_esporte = []
dois_esporte = []

esporte = []

while True:
    aluno = input("nome do aluno: ")
    if aluno == '0':
        break
    esporte1 = input("primeiro esporte: ").lower()
    esporte2 = input("segundo esporte: ").lower()
    
    if esporte2 == 'no':
        um_esporte.append(aluno)
        esporte.append(esporte1)
    else:
        dois_esporte.append(aluno)
        esporte.append(esporte1)
        esporte.append(esporte2)
        

matriculados.append([um_esporte, dois_esporte, esporte])
fut = esporte.count('futebol')
basca = esporte.count('basquete')
natacao = esporte.count('natacao')
volei = esporte.count('volei')

print(f"alunos matriculados: {len(um_esporte) + len(dois_esporte)}")
print(f"os alunos que possuem o direito do desconto são {dois_esporte}")
print(f"numero de alunos por modalidade: {fut} em futebol, {basca} em basquete, {natacao} em natacao e {volei} em volei")
