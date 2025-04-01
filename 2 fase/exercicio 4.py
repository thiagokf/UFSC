class Biblioteca:
    def __init__(self, livros = []):
        self.livros = livros


    def incluir_livro(self, Livro,livro):
        if isinstance (livro, Livro):
            self.livros.append(livro)

    def exclir_livro(self, livro, Livro):
        if isinstance(livro, Livro):
            self.livros.remove(Livro)

class Autor:
    def __init__(self, codigo, nome):
        self.nome = nome
        self.codigo = codigo

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.nome = nome

    @property
    def codigo(self):
        return self.codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.codigo = codigo


class Editora:
    def __init__(self, codigo, nome):
        self.nome = nome
        self.codigo = codigo

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.nome = nome

    @property
    def codigo(self):
        return self.codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.codigo = codigo

class Capitulo:
    def __init__(self, codigo, nome):
        self.nome = nome
        self.codigo = codigo

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.nome = nome

    @property
    def codigo(self):
        return self.codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.codigo = codigo


class Livro:
    def __init__(self, codigo, titulo, ano, editora: Editora, autor: Autor, numero_capitulo, titulo_capitulo):
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano
        self.editora = editora
        self.autores = [autor]
        self.capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    @property
    def codigo(self):
        return self.codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo,int):
            self.codigo = codigo
    
    @property
    def titulo(self):
        return self.titulo
    
    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo,str):
            self.titulo = titulo

    @property
    def ano(self):
        return self.ano
    
    @ano.setter
    def ano(self, ano):
        if isinstance(ano,int):
            self.ano = ano

    @property
    def editora(self):
        return self.editora
    
    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.editora = editora

    @property
    def editora(self):
        return self.editora
    
    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.editora = editora
    
    @property
    def editora(self):
        return self.editora
    
    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.editora = editora
    
    @property
    def autores(self):
        return self.__autores
        
    def incluir_autor(self, autor):
        for autor in self.__autores:
            if Autor.nome == autor:
                print('esse autor ja foi incluido')
            else:
                self.__autores.append(Autor.nome())

    def excluir_autor(self, autor):
        self.autores.remove(autor)

    def incluir_capitulo(self, )
        
