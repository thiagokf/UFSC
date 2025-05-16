class Capitulo:
    def __init__(self, numero, titulo):
        self.__titulo = titulo
        self.__numero = numero

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        if isinstance(numero, int):
            self.__numero = numero
