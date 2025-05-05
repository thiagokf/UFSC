from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__personagems = []
        self.__baralho = []

    @property
    def personagems(self):
        if isinstance(self.__personagems, list):
            return self.__personagems
    
    @property
    def baralho(self):
        if isinstance(self.__baralho, list):
            return self.__baralho

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        perso = Personagem(energia, habilidade, velocidade, resistencia, tipo)

        self.__personagems.append(perso)
        return self.__personagems
    
    def inclui_carta_no_baralho(self, personagem):
        carta = Carta(personagem)
        self.__baralho.append(carta)

    def jogada(self, mesa: Mesa):
        if mesa.cartaJogador1.valor_total_carta > mesa.cartaJogador2.valor_total_carta:
            mesa.jogador1.incluir_carta_na_mao(mesa.cartaJogador1)
            mesa.jogador1.incluir_carta_na_mao(mesa.cartaJogador2)

            if mesa.jogador2.mao == 0:
                return mesa.jogador1

        if mesa.cartaJogador1.valor_total_carta < mesa.cartaJogador2.valor_total_carta:
            mesa.jogador2.incluir_carta_na_mao(mesa.cartaJogador1)
            mesa.jogador2.incluir_carta_na_mao(mesa.cartaJogador2)

            if mesa.jogador1.mao == 0:
                return mesa.jogador2

        return None
            
