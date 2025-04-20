# # a fazer
from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict
class ControladorChamados(AbstractControladorChamados):
    
        
    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        return sum(1 for chamado in self.__chamados if chamado.tipo.codigo == tipo.codigo)


# # feito

from abc import ABC, abstractmethod, abstractproperty
from datetime import date as Date


class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def codigo(self) -> int:
        pass
    
    @property
    @abstractmethod
    def nome(self) -> str:
        pass

class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
class Tecnico(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)

class Cliente(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)


        
class AbstractTipoChamado(ABC):

    @property
    @abstractmethod
    def codigo(self) -> int:
        pass

    @property
    @abstractmethod
    def descricao(self) -> str:
        pass

    @property
    @abstractmethod
    def nome(self) -> str:
        pass

class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__nome = nome
        self.__chamados = []

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
        self.__descricao == descricao

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome == nome

    @property
    def chamados(self):
        return self.__chamados
        
class AbstractChamado(ABC):
    @property
    @abstractmethod
    def cliente(self) -> Cliente:
        pass

    @property
    @abstractmethod
    def data(self) -> Date:
        pass

    @property
    @abstractmethod
    def descricao(self) -> str:
        pass

    @property
    @abstractmethod
    def prioridade(self) -> int:
        pass

    @property
    @abstractmethod
    def tecnico(self) -> Tecnico:
        pass

    @property
    @abstractmethod
    def tipo(self) -> TipoChamado:
        pass

    @property
    @abstractmethod
    def titulo(self) -> str:
        pass
    
class Chamado(AbstractChamado):
    def __init__(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        self.__data = Date
        self.__cliente = Cliente
        self.__tecnico = Tecnico
        self.__titulo = titulo
        self.__descricao = descricao
        self.__prioridade = prioridade
        self.__tipo = TipoChamado
    
    @property
    def data(self):
        if isinstance(data, Date):
            return self.__data
    
    @property
    def cliente(self):
        if isinstance(cliente, Cliente):
            return self.__cliente
        
    @property
    def tecnico(self):
        if isinstance(tecnico, Tecnico):
            return self.__tecnico    
        
    @property
    def titulo(self):
        if isinstance(titulo, str):
            return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
        
    @property
    def descricao(self):
        if isinstance(descricao, str):
            return self.__descricao
        
    @descricao.setter
    def titulo(self, descricao):
        self.__descricao = descricao
        
    @property
    def prioridade(self):
        if isinstance(prioridade, int):
            return self.__prioridade
    
    @prioridade.setter
    def titulo(self, prioridade):
        self.__prioridade = prioridade
        
    @property
    def tipo(self):
        if isinstance(tipo, TipoChamado):
            return self.__tipo

class AbstractControladorPessoas(ABC):
    # @return retorna a lista de clientes
    @abstractproperty
    @property
    def clientes(self) -> list:
        pass

    # @return retorna a lista de tecnicos
    @abstractproperty
    @property
    def tecnicos(self) -> list:
        pass

    # Permite a inclusao de um novo cliente na lista de clientes
    # @param codigo codigo do Cliente
    # @param nome nome do Cliente
    # @return retorna o cliente inserido
    @abstractmethod
    def inclui_cliente(self, codigo :int, nome :str) -> Cliente:
        pass

    # Permite a inclusao de um novo tecnico na lista de tecnicos
    # @param codigo codigo do tecnico
    # @param nome nome do tecnico
    # @return retorna o tecnico inserido
    @abstractmethod
    def inclui_tecnico(self, codigo :int, nome :str) -> Tecnico:
        pass

class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def tecnicos(self):
        return self.__tecnicos
    
    def incluir_cliente(self, nome: str, codigo: int):
        c = Cliente(nome, codigo)
        for i in self.__clientes:
            if c.nome == i.nome and c.codigo == i.codigo:
                print('esse cliente ja foi adicionado')
            else:
                self.__clientes.append(c)
    
    def incluir_tecnico(self, nome: str, codigo: int):
        t = Tecnico(nome, codigo)
        for i in self.__clientes:
            if t.nome == i.nome and t.codigo == i.codigo:
                print('esse cliente ja foi adicionado')
            else:
                self.__tecnicos.append(t)
        return self.__tecnicos
    
class AbstractControladorChamados(ABC):
    # Retorna o total de chamados registrados para o TipoChamado recebido como parametro
    # @param tipo TipoChamado
    # @return int com a quantidade total dos chamados daquele tipo
    @abstractmethod
    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        pass

    # Permite incluir um novo chamado na lista de Chamados. O chamado incluido eh retornado como um Chamado
    # @param data data do chamado em formato Date
    # @param cliente referencia para o Cliente do chamado
    # @param tecnico referencia para o Tecnico do chamado
    # @param titulo titulo do chamado
    # @param descricao descricao do chamado
    # @param prioridade prioridade do chamado
    # @param tipo tipo do chamado (TipoChamado)
    # @return retorna o chamato cadastrado
    @abstractmethod
    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        pass

    # Permite incluir um novo TipoChamado na lista de Tipos de Chamado. O TipoChamado incluido eh retornado como um TipoChamado
    # @param codigo codigo do Tipo Chamado
    # @param nome nome do Tipo Chamado
    # @param descricao descricao do Tipo Chamado
    # @return retorna o Tipo Chamado cadastrado
    @abstractmethod
    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        pass

    # Retorna os tipos de chamado que foram cadastrados no controlador pelo metodo inclui_tipochamado
    @property
    @abstractmethod
    def tipos_chamados(self):
        pass

class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.tipoChamados = [Chamado]
        
    def total_chamados_por_tipo(self, tipo: TipoChamado):
        return len(tipo.chamados)
    
    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        c = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
        tipo.chamados.append(c)
        return c
    
    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str):
        t = TipoChamado(codigo, descricao, nome)
        return t
    
    def tipos_chamados(self):
        return self.tipoChamados
        
# # teste # #
tc = TipoChamado(1,1,"Bug")
print(tc.codigo,tc.descricao,tc.nome) # 1 1 Bug
c = Cliente("Cliente", 2)
print(c.nome,c.codigo) # Cliente 2
t = Tecnico("Tecnico", 2)
print(t.nome,t.codigo) # Tecnico 2
ch = Chamado(Date.today(), c, t, "titulo", "descricao", 4, tc)
print(ch.tipo.nome) # Bug

cp = ControladorPessoas()
cp.inclui_cliente(1, "cli")
cp.inclui_tecnico(1, "tec")
for c in cp.clientes: # cli
    print(c.nome)
for t in cp.tecnicos: # tec
    print(t.nome)

cc = ControladorChamados()
print(cc.total_chamados_por_tipo(tc)) # 0
