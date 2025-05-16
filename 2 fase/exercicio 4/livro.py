
class Livro:
    def __init__(self, codigo, titulo, ano, editora: Editora, autor: Autor, numero_capitulo, titulo_capitulo):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__numero_capitulo = numero_capitulo
        self.__titulo_capitulo = titulo_capitulo
        self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo,int):
            self.__codigo = codigo
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo,str):
            self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if isinstance(ano,int):
            self.__ano = ano

    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora

    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora
    
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora 
    @property
    def autores(self):
        if isinstance(autor, Autor):
            return self.__autores
        
    def incluir_autor(self, autor):
        aux = 0
        if isinstance(autor, Autor):
            for i in range(len(self.__autores)):
                if autor.nome == self.__autores[i].nome and autor.codigo == self.__autores[i].codigo:
                    aux += 1
                if aux == 1:
                    return print('deu merda')
                    
                self.__autores.append(autor)
            #add o objeto autor (add nome = autor.nome)
    def excluir_autor(self, autor):
        self.__autores.remove(autor)
        
    @property
    def capitulos(self):
        return self.__capitulos

    def incluir_capitulo(self, numero_capitulo, titulo_capitulo):
        aux = 0
        for i in range(len(self.__capitulos)):
            if titulo_capitulo == self.__capitulos[i].titulo and numero_capitulo == self.capitulos[i].numero:          
                aux += 1
            if aux == 1:
                return 'esse capitulo ja foi adicionado'
                
        cap = Capitulo(numero_capitulo,titulo_capitulo)
        self.__capitulos.append(cap)

        
            
    def excluir_capitulo(self, titulo_capitulo):
        for i in range(len(self.__capitulos)):
            if titulo_capitulo == self.__capitulos[i].titulo:
                return self.__capitulos.pop(i)
        
            
    def find_capitulo_by_titulo(self, titulo_capitulo):
        for i in range(len(self.__capitulos)):
            if titulo_capitulo == self.__capitulos[i].titulo:
                return self.__capitulos[i]
