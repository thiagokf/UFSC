from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador): 
    def __init__(self, andar_atual: int, total_andares_predio: int,
                 pessoas_no_elevador: int, total_pessoas: int):
        self.__andar_atual = andar_atual
        self.__total_andares_predio = total_andares_predio
        self.__pessoas_no_elevador = pessoas_no_elevador
        self.__total_pessoas = total_pessoas

    # elevadorJahNoTerreo    
    def descer(self):
        if self.__andar_atual - 1 < 0:
            raise ElevadorJahNoTerreoException()
        self.__andar_atual - 1

    # elevadorCheio    
    def entra_pessoa(self):
        if self.__pessoas_no_elevador + 1 > self.__capacidade:
            raise ElevadorCheioException()
        self.__pessoas_no_elevador + 1
        
    # elevadorVazio
    def sai_pessoa(self) -> str:
        if self.__pessoas_no_elevador - 1 < 0:
            raise ElevadorJahVazioException()
        self.__pessoas_no_elevador - 1
        
    # elevador ja no maximo
    def subir(self) -> str:
        if self.__andar_atual + 1 > self.__total_andares_predio:
            raise ElevadorJahNoUltimoAndarException()
        self.__andar_atual += 1
        
    @property
    def capacidade(self) -> int:
        if isinstance(self.__capacidade, int)
        return self.__capacidade
    
    @property
    def total_pessoas(self) -> int:
        if isinstance(self.__total_pessoas, int)
        return self.__total_pessoas
    
    @property
    def total_andares_predio(self) -> int:
        if isinstance(self.__total_andares_predio, int)
        return self.__total_andares_predio
    
    @property
    def andar_atual(self) -> int:
        if isinstance(self.__andar_atual, int)
        return self.__andar_atual
    
    @total_andares_predio.setter
    def total_andares_predio(self, total_andares_predio: int):
        self.__total_andares_predio = total_andares_predio
