from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    def inicializar_elevador(self, andar_atual: int, total_andares_predio: int,
                             capacidade: int, total_pessoas: int):
        self.__elevador = Elevador(andar_atual, total_andares_predio,
                                   capacidade, total_pessoas)

    def subir(self):
        return self.__elevador.subir()

    def descer(self) -> str:
        return self.__elevador.descer()

    def entra_pessoa(self) -> str:
        return self.__elevador.entra_pessoa()

    def sai_pessoa(self) -> str:
        return self.__elevador.sai_pessoa()

    @property
    def elevador(self) -> Elevador:
        return self.__elevador
