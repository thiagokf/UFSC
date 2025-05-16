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
