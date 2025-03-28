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


###############################

class Venda:
    def __init__(self, codigo, cliente, descricao, pacote, quantidade):
        if isinstance (cliente, Cliente):
            self.__cliente = cliente
        if isinstance (pacote, PacoteViagem):
            self.__pacote = pacote
            
        self.__codigo = codigo
        self.__quantidade = quantidade
        self.__descricao = descricao
        
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self):
        if isinstance (cliente, Cliente):
            self.cliente == cliente
        else:
            print('erro')
     
    @property
    def pacote(self):
        return self.__pacote
    
    @pacote.setter
    def pacote(self):
        if isinstance (pacote, PacoteViagem):
            self.pacote == pacote
        else:
            print('erro')
             
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self):
        self.__codigo = codigo
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self):
        self.__descricao = descricao
         
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self):
        self.__quantidade = quantidade

    def preco_total(self):
        preco = self.__pacote.custo_unitario * self.__quantidade
        
        
class Cliente:
    def __init__(self, nome, fone, email):
        self.__nome = nome
        self.__fone = fone
        self.__email = email
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self):
        self.__nome = nome
    
    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self):
        self.__fone = fone
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self):
        self.__email = email
        
class PacoteViagem:
    def __init__(self, origem, destino, duracao, custo_unitario):
        self.__origem = origem
        self.__destino = destino
        self.__duracao = duracao
        self.__custo_unitario = custo_unitario
        
    @property
    def origem(self):
        return self.__origem
    
    @origem.setter
    def origem(self):
        self.__origem = origem
        
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self):
        self.__destino = destino
        
    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self):
        self.__duracao = duracao
        
    @property
    def custo_unitario(self):
        return self.__custo_unitario
    
    @custo_unitario.setter
    def custo_unitario(self):
        self.__custo_unitario = custo_unitario
        
    
cliente = Cliente('thiago', '123', 'oie')
pacot = PacoteViagem('floripa', 'descanso', 3, 100)
venda = Venda('1234', cliente, 'é bem legal', pacot, 2)

# testando cliente

print('-----teste cliente-----')
print(cliente.nome)
print(cliente.fone)
print(cliente.email)

print('-----teste pacote-----')
print(pacot.origem)
print(pacot.destino)
print(pacot.duracao)
print(pacot.custo_unitario)

print('-----teste venda!-----')
print(venda.codigo)
print(venda.cliente.nome, venda.cliente.fone, venda.cliente.email)
print(venda.descricao)
print(venda.pacote.origem, venda.pacote.destino, venda.pacote.duracao, venda.pacote.custo_unitario)
print(venda.quantidade)
print(venda.preco_total())
