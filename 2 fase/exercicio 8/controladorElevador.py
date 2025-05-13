from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException


class ControladorElevador(AbstractControladorElevador):
    def __init__(self, elevador: Elevador):
        self.__elevador = elevador
    
    def inicializar_elevador(self, andar_atual: int, total_andares_predio: int,
                             capacidade: int, total_pessoas: int):
        elevador = Elevador(andar_atual, total_andares_predio, capacidade, total_pessoas)
    
    def subir(self):
        try:
            aux = self.__andar_atual + 1
            if aux < self.__total_andares_predio:
                self.__andar_atual = aux
                return self.__andar_atual
        except ElevadorJahNoUltimoAndarException as e:
            return print(e)

        def descer(self) -> str:
        try:
            aux = self.__andar_atual - 1
            if aux < 0:
                self.__andar_atual = aux
                return "desceu!"
        except ElevadorJahNoTerreoException as e:
            print(e)

    '''
    Entra uma pessoa no Elevador. Se nao for possivel permitir a entrada da pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorCheioException
    '''
    @abstractmethod
    def entra_pessoa(self) -> str:
        return self.__elevador.entra_pessoa()
    '''
    Sai uma pessoa no Elevador. Se nao for possivel permitir a saida de uma pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahVazioException
    '''
    @abstractmethod
    def sai_pessoa() -> str:
        try:
            aux = self.__pessoas_no_elevador - 1
            if aux > 0:
                self.__pessoas_no_elevador = aux
                return "saiu!"
        except ElevadorJahVazioException as e:
            print(e)
	
    '''
    @return Elevador
    '''
    @property
    @abstractmethod
    def elevador(self) -> Elevador:
    	if isinstance
