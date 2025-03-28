class Aluno():
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

# preciso aprender melhor essa parte
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        if (isinstance(nome, str)):
            self.__nome = nome
        else:
            print('tem q ser string feio')
    
    def mostrar_dados(self):
        return f'{self.__nome} - {self.__idade} anos - matricula: {self.__matricula}'

    def faz_aniversario(self):
        self.__idade += 1

aluno = Aluno('thiago', 18, 123)
n = Aluno('nicole', 19, 234)
print(aluno.mostrar_dados())
aluno.faz_aniversario()
print(aluno.mostrar_dados())
print('|------------------------------------|')
print(n.mostrar_dados())

##############################################

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
class Cliente(Pessoa):
    def __init__(self, cod, nome):
        super().__init__(nome)
        self.__cod = cod

    @property
    def cod(self):
        return self.__cod
alguem = Pessoa('nicole')

print(alguem.nome)

cliente = Cliente(1, 'nicole')

print(cliente.cod)
print(cliente.nome)
