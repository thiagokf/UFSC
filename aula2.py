class Aluno:
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco
        

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self):
        self.__nome = nome
        
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self):
        self.__endereco = endereco
        
class Professor:
    def __init__(
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self):
        self.__endereco = endereco
        
    @property
    def orientando(self):
        return self.__orientando
    
    @orientando.setter   
    def orientando(self, orientando):
        if not isinstance(orientando, Aluno):
            print('erro')
            
        else:
            self.__orientando = orientando

a = Aluno('thiago', 'lagoa')
p = Professor('Thais', 'corrego', a)


print(p.orientando.nome)self, nome, endereco, orientando):
        if isinstance(orientando, Aluno):
            self.__orientando = orientando
        self.__nome = nome
        self.__endereco = endereco
    
    @property
    def nome(self):
        return self.__nome 
    
    @nome.setter
    def nome(self):
        self.__nome = nome
        
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self):
        self.__endereco = endereco
        
    @property
    def orientando(self):
        return self.__orientando
    
    @orientando.setter   
    def orientando(self, orientando):
        if not isinstance(orientando, Aluno):
            print('erro')
            
        else:
            self.__orientando = orientando

a = Aluno('thiago', 'lagoa')
p = Professor('Thais', 'corrego', a)


print(p.orientando.nome)

