class Biblioteca:
    def __init__(self):
        self.__livros = []
        
    def incluir_livro(self, Livro):
        if Livro not in self.__livros:
            self.__livros.append(Livro)

    def excluir_livro(self, Livro):
        if Livro in self.__livros:
            self.__livros.remove(Livro)
        
    @property
    def livros(self):
        return self.__livros

class Autor:
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
            

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo


class Editora:
    def __init__(self, codigo, nome):
        self.__nome = nome
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

class Capitulo:
    def __init__(self, numero_capitulo, titulo_capitulo):
        self.__titulo_capitulo = titulo_capitulo
        self.__numero_capitulo = numero_capitulo

    @property
    def titulo_capitulo(self):
        return self.__titulo_capitulo
    
    @titulo_capitulo.setter
    def titulo_capitulo(self, titulo_capitulo):
        if isinstance(titulo_capitulo, str):
            self.__titulo_capitulo = titulo_capitulo

    @property
    def numero_capitulo(self):
        return self.__numero_capitulo
    
    @numero_capitulo.setter
    def numero_capitulo(self, numero_capitulo):
        if isinstance(numero_capitulo, int):
            self.__numero_capitulo = numero_capitulo


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
        return self.__autores
        
    def incluir_autor(self, autor):
        if autor.nome in self.__autores:
            print('esse autor ja foi incluido')
        else:
            self.__autores.append(autor)
            #add o objeto autor (add nome = autor.nome)
    def excluir_autor(self, autor):
        self.__autores.remove(autor)
        
    @property
    def capitulos(self):
        return self.__capitulos

    def incluir_capitulo(self, numero_capitulo, titulo_capitulo):
        return self.__capitulos.append(numero_capitulo, titulo_capitulo)

# >> cadastro das informaçoes: ok <<
a1 = Autor(1, "Machado de Assis")
a2 = Autor(2, "Ariano Suassuna")
ed1 = Editora(1, "Via Leitura")
l1 = Livro(42, "Dom Casmurro", 2015,
ed1, a1, 1, "Do Título")
l2 = Livro(1, "Memórias Póstumas de Brás Cubas", 1958,
ed1, a2, 1, "Do Título")

# >> print e setters: ok <<
# print(l1.codigo, l1.titulo, l1.ano,
# l1.editora.nome,l1.autores[0].nome,
# l1.capitulos[0].titulo_capitulo)

# l1.codigo = 1
# l1.titulo = "Memórias Póstumas de Brás Cubas"
# l1.ano = 2010

# print(l1.codigo, l1.titulo, l1.ano,
# l1.editora.nome,l1.autores[0].nome,
# l1.capitulos[0].titulo_capitulo)


# >> inclusão de autores: ok <<
# l1.incluir_autor(a2)
# for autor in l1.autores:
#     print(autor.nome)


biblio = Biblioteca()
biblio.incluir_livro(l1)
biblio.incluir_livro(l2)

for livro in biblio.livros:
    print(livro.titulo)
    
biblio.excluir_livro(l1)

for livro in biblio.livros:
    print(livro.titulo)


