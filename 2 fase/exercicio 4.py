class Biblioteca:
    def __init__(self):
        self.__livros = []
        
    def incluir_livro(self, livro):
        if isinstance(livro, Livro):
            for i in self.__livros:
                if i.codigo == livro.codigo:
                    return 'deu boga'
            self.__livros.append(livro)

    def excluir_livro(self, livro):
        for i in self.__livros:
            self.__livros.remove(livro)
        
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

        
            

# >> cadastro das informaçoes: ok <<
a1 = Autor(1, "Machado de Assis")
a2 = Autor(2, "Ariano Suassuna")
a3 = Autor(1,"Machado de Assis")
ed1 = Editora(1, "Via Leitura")
l1 = Livro(42, "Dom Casmurro", 2015,
ed1, a1, 1, "Do Título")
l2 = Livro(1, "Memórias Póstumas de Brás Cubas", 1958,
ed1, a2, 1, "Do Título")

# l2.incluir_capitulo(1, 'oi')
# l2.incluir_capitulo(1, 'oi')
# 
# print(l2.capitulos)

# l1.incluir_autor(a3)
# print(l1.autores)
# >>> encontrar capitulo pelo nome: OK <<<
#print(l2.find_capitulo_by_titulo('tchau').titulo)

# >>> incluir e excluir capitulo: OK <<<
#print(l2.capitulos)
# l2.incluir_capitulo()
#l2.excluir_capitulo('oie')

#print(l2.capitulos)

#for i in range(2):
#    print(l2.capitulos[i].titulo)
# l1.incluir_capitulo()
# print(l1.capitulos)
# 
# l2.excluir_capitulo()
# print(l2.capitulos)

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
#a3 = Autor(1, 'tiagao')
#l1.incluir_autor(a2)
#l1.incluir_autor(a3)
#for autor in l1.autores:
#    print(autor.nome)
#    print(autor)


biblio = Biblioteca()
biblio.incluir_livro(l1)
biblio.incluir_livro(l2)
# 
for livro in biblio.livros:
    print(livro.titulo)

biblio.excluir_livro(l2)

for livro in biblio.livros:
    print(livro.titulo)

# 
# 
# for livro in biblio.livros:
#     print(livro.titul
