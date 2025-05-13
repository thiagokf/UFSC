class ElevadorJahNoUltimoAndarException(Exception):
    def __init__(self):
        self.mensagem = "o elevador já esta no ultimo andar!!!"
        super().__init__(self.mensagem)

class ElevadorJahVazioException(Exception):
    def __init__(self):
        self.mensagem = "o elevador esta vazio!!!"
        super().__init__(self.mensagem)

class ElevadorJahNoTerreoException(Exception):
    def __init__(self):
        self.mensagem = "o elevador já esta no terreo!!!"
        super().__init__(self.mensagem)

class ElevadorCheioException(Exception):
    def __init__(self):
        self.mensagem = "o elevador esta cheio!!!"
        super().__init__(self.mensagem)
