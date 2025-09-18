class Elemento:
    def __init__(self, valor):
            self.__valor = valor
            self.__ant = None
            self.__prox = None
            self.__posicao = None

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, prox):
        self.__prox = prox
    
    @property
    def ant(self):
        return self.__ant

    @ant.setter
    def ant(self, ant):
        self.__ant = ant
    
    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

class Cursor:
    def __init__(self):
        self.__posicao = 0
        self.__aponta = None
    
    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao
    
    @property
    def aponta(self):
        return self.__aponta

    @aponta.setter
    def aponta(self, aponta):
        self.__aponta = aponta

class ListaEncadeada:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__cursor = Cursor()
        self.__tamanho_atual = 0
        self.__inicio = None
        self.__fim = None
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @property
    def tamanho_atual(self):
        return self.__tamanho_atual
    
    @tamanho_atual.setter
    def tamanho_atual(self, tamanho_atual):
        self.__tamanho_atual = tamanho_atual
    
    @property
    def inicio(self):
        return self.__inicio
    
    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio
    
    @property
    def fim(self):
        return self.__fim
    
    @fim.setter
    def fim(self, fim):
        self.__fim = fim
    
    @property
    def cursor(self):
        return self.__cursor
    
    @cursor.setter
    def cursor(self, cursor):
        self.__cursor = cursor
    
    def ajuste_de_posicao(self, i):
        while True:
                i.posicao += 1
                if i.prox == None:
                    return
                i = i.prox

    def inserir_antes_do_atual(self, elemento):
        atual = self.__cursor.aponta
        if atual == None:
            self.__inicio = elemento
            self.__fim = elemento
            self.__cursor.aponta = elemento
            elemento.posicao = 1
            return
        if atual.ant == None:
            elemento.prox = self.__inicio
            self.__inicio = elemento
            elemento.posicao = 1
            atual.ant = elemento
            self.ajuste_de_posicao(atual)
            return
        atual.ant.prox = elemento
        elemento.ant = atual.ant
        atual.ant = elemento
        elemento.prox = atual
        elemento.posicao = atual.posicao
        self.ajuste_de_posicao(atual)
    
    def inserir_depois_do_atual(self, elemento):
        atual = self.__cursor.aponta
        if atual == None:
            self.__inicio = elemento
            self.__fim = elemento
            elemento.posicao = 1
            return
        if atual.prox == None:
            self.__fim = elemento
        elemento.posicao = atual.posicao + 1
        elemento.prox = atual.prox
        if elemento.prox != None:
            elemento.prox.ant = elemento
        atual.prox = elemento
        elemento.ant = atual
        if elemento.prox != None:
            self.ajuste_de_posicao(elemento.prox)

        return
    def inserir_como_primeiro(self, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            self.ir_para_primeiro()
            self.inserir_antes_do_atual(elemento)
            self.__tamanho_atual += 1
        else:
            print("lista cheia")

    def inserir_como_ultimo(self, elemento):
        if self.__tamanho_atual + 1 <= self.__tamanho:
            self.ir_para_ultimo()
            self.inserir_depois_do_atual(elemento)
            self.__tamanho_atual += 1
        else:
            print("lista cheia")

    def ir_para_ultimo(self):
        self.__cursor.posicao = self.__tamanho_atual
        self.__cursor.aponta = self.__fim

    def ir_para_primeiro(self):
        self.__cursor.posicao = 1
        self.__cursor.aponta = self.__inicio
        return self.__cursor.aponta

    def acessar_atual(self):
        return self.__cursor.aponta
# inserindo como primeiro (OK!)
# inserindo como ultimo (Ok!)
# inserindo depois do apontado (Ok!)
# inserindo antes do apontado (Ok!)

a = ListaEncadeada(5)
n = Elemento('niki')
t = Elemento('thiago')
ni = Elemento('nikinha')
p = Elemento('bola')
a.inserir_como_primeiro(n) # niki primiero
a.inserir_antes_do_atual(t) #thiago primeiro
a.inserir_antes_do_atual(ni) #thiago ainda primeiro, nikinha atras da niki
a.inserir_antes_do_atual(p)

print("--thiago--")
print(t.posicao)
print(t.ant)
print(t.prox.valor)
print("--nikinha--")
print(ni.posicao)
print(ni.ant.valor)
print(ni.prox.valor)
print("--p--")
print(p.posicao)
print(p.ant.valor)
print(p.prox.valor)
print("--niki--")
print(n.posicao)
print(n.ant.valor)
print(n.prox)
