from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException
from comandoInvalidoException import ComandoInvalidoException


class Elevador(AbstractElevador):
    def __init__(self, andar_atual: int, total_andares_predio: int,
                 capacidade: int, total_pessoas: int):
        verif = [andar_atual, total_andares_predio, capacidade, total_pessoas]
        for i in verif:
            if not isinstance(i, int) or i < 0:
                raise ComandoInvalidoException()
        if andar_atual > total_andares_predio:
            raise ComandoInvalidoException()
        elif total_pessoas > capacidade:
            raise ComandoInvalidoException()
        self.__andar_atual = andar_atual
        self.__total_andares_predio = total_andares_predio
        self.__capacidade = capacidade
        self.__total_pessoas = total_pessoas

    def descer(self):
        if self.__andar_atual - 1 < 0:
            raise ElevadorJahNoTerreoException()
        self.__andar_atual -= 1

    def entra_pessoa(self):
        if self.__total_pessoas + 1 > self.__capacidade:
            raise ElevadorCheioException()
        self.__total_pessoas += 1

    def sai_pessoa(self) -> str:
        if self.__total_pessoas - 1 < 0:
            raise ElevadorJahVazioException()
        self.__total_pessoas -= 1

    def subir(self) -> str:
        if self.__andar_atual + 1 > self.__total_andares_predio:
            raise ElevadorJahNoUltimoAndarException()
        self.__andar_atual += 1

    @property
    def capacidade(self) -> int:
        if not isinstance(self.__capacidade, int) or self.__capacidade < 0:
            raise ComandoInvalidoException()
        return self.__capacidade

    @property
    def total_pessoas(self) -> int:
        return self.__total_pessoas

    @property
    def total_andares_predio(self) -> int:
        return self.__total_andares_predio

    @property
    def andar_atual(self) -> int:
        return self.__andar_atual

    @total_andares_predio.setter
    def total_andares_predio(self, total_andares_predio: int):
        self.__total_andares_predio = total_andares_predio
