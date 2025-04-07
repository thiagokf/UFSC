class Pessoa:
    def __init__(self , nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__nome = cpf


class Dependente(Pessoa):
    def __init__(self,nome, cpf):
        super().__init__(nome, cpf)


class Cargo:
    def __init__(self, salario, descricao):
        self.__salario = salario
        self.__descricao = descricao

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
      
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo: Cargo):
        super().__init__(nome, cpf)
        if isinstance(cargo, Cargo):
            self.__cargo = cargo
        self.__dependentes = []

    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def dependentes(self):
        return self.__dependentes
    
    def add_dependente(self, nome, cpf):
        dup = False
        for dep in self.__dependentes:
            if dep.cpf == cpf:
                print('dependente ja adicionado')
                dup = True
            if dup == True:
                return
        f = Dependente(nome, cpf)
        self.__dependentes.append(f)
        
    def rem_dependente(self, cpf):
        for i in self.__dependentes:
            if i.cpf == cpf:
                self.__dependentes.remove[i]


c1 = Cargo(5300.00, "Gerente")
c2 = Cargo(30000.00, "Desenvolvedor")

funcionarios = []
f1 = Funcionario("Iza","0001", c1)
funcionarios.append(f1)
f2 = Funcionario("Juca","0002", c2)
funcionarios.append(f2)
f3 = Funcionario("Maria","0042", c2)
funcionarios.append(f3)

f1.add_dependente("Jose", "111")
f1.add_dependente("Jose", "111")
f1.add_dependente("Joana", "222")

print("Funcionarios da empresa:")
for f in funcionarios:
    print(f.nome, f.cpf, f.cargo.descricao, f.cargo.salario)

print("\nDependentes da ", f1.nome)
for dep in f1.dependentes:
    print(dep.nome)
    
    
#implementar classe abstrata depois
    

