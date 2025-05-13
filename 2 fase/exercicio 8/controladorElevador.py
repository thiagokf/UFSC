from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException


class ControladorElevador(AbstractControladorElevador):
	def __init__(self, elevador: Elevador):
	self.__elevador = elevador
	
	def inicializar_elevador(self, andar_atual: int, total_andares_predio: int, capacidade: int, total_pessoas: int):
	elevador = Elevador(andar_atual, total_andares_predio, capacidade, total_pessoas)
	
	def subir(self):
		return self.__elevador.subir()
	
	def descer(self) -> str:
		return self.__elevador.descer()
		
	def entra_pessoa(self) -> str:
		return self.__elevador.entra_pessoa()

	def sai_pessoa() -> str:
		return self.__elevador.sai_pessoa()
		
	@property
	def elevador(self) -> Elevador:
	if isinstance(elevador, Elevador):
		return self.__elevador
