from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):
    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    @property
    def personagem(self) -> Personagem:
        if isinstance(self.__personagem, Personagem):
            return self.__personagem
        
    def valor_total_carta(self):
        sum = 0
        sum = self.__personagem.energia + self.__personagem.habilidade
        sum += self.personagem.resistencia + self.__personagem.velocidade
        return sum
    
