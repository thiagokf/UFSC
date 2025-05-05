from AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    #Construtor fornecido, nao deve ser alterado
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        self.__tipo = tipo
        self.__energia = energia
        self.__habilidade = habilidade
        self.__velocidade = velocidade
        self.__resistencia = resistencia

    @property
    def tipo(self) -> Tipo:
        if isinstance(self.__tipo, Tipo):
            return self.__tipo

    @property
    def energia(self) -> int:
        if isinstance(self.__energia,  int):
            return self.__energia

    @property
    def habilidade(self) -> int:
        if isinstance(self.__habilidade,  int):
            return self.__habilidade

    @property
    def velocidade(self) -> int:
        if isinstance(self.__velociade,  int):
            return self.__velocidade

    @property
    def resistencia(self) -> int:
        if isinstance(self.__resistencia,  int):
            return self.__resistencia 
