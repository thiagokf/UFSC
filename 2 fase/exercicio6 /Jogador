from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome):
        self.__nome = nome
        self.__mao = []

    @property
    def nome(self):
        if isinstance(self.__nome, str):
            return self.__nome

    @property
    def mao(self):
        return self.__mao

    def incluir_carta_na_mao(self, carta: Carta):
        if isinstance(carta, Carta):
            self.__mao.append(carta)

    def baixa_carta_da_mao(self, carta: Carta):
        if len(self.__mao) > 0:
            self.__mao.pop(carta)
