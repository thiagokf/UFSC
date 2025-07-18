from cliente import Cliente
from pacote_viagem import PacoteViagem


class Venda:
    def __init__(self, codigo, cliente, descricao, pacote, quantidade):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(pacote, PacoteViagem):
            self.__pacote = pacote
        self.__codigo = codigo
        self.__quantidade = quantidade
        self.__descricao = descricao

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        else:
            print('erro')

    @property
    def pacote(self):
        return self.__pacote

    @pacote.setter
    def pacote(self, pacote):
        if isinstance(pacote, PacoteViagem):
            self.__pacote = pacote
        else:
            print('erro')

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def preco_total(self):
        return self.__pacote.custo_unitario * self.__quantidade
