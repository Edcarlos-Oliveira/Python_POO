print('¬'*10, 'Trabalhando com Herança', '¬'*10)
class Pai(object):
    # Criando o construtor
    def __init__(self, nome, idade):
        self.n = nome
        self.i = idade

    # Método para mostrar
    def mostreP(self):
        print(f'Prazer, sou {self.n} e tenho {self.i} anos.')

# Criando o objeto
dados = Pai(str(input('Nome do Pai: ')), int(input('Idade do Pai: ')))
dados.mostreP()
print()

print('!'*10, 'Criando a classe filho', '!'*10)
class Filho(Pai):
    def mostrarF(self):
        print('Chamado a classe filho')

# Detalhes de filho
fil = Filho(str(input('Nome do Filho: ')), int(input('Idade do Filho: ')))

# Chamando a função da classe pai
fil.mostreP()

# Chamando a função da classe filho
fil.mostrarF()
print()

print('*'*10, 'Exemplo 2 de herança chamando o construtor Pai', '*'*10)
class Super_Pai(object):
    def __init__(self, nome, id):
        self.n = nome
        self.id = id

    # Criando o método mostrar
    def mostrar(self):
        print(f'Nome {self.n} e id {self.id}.')

# Criando a classe filho
class Super_Filho(Super_Pai):
    def __init__(self, nome, id, anoN, idade):
        self.an = anoN
        self.i = idade

        # Chamando o construtor Pai
        Super_Pai.__init__(self, nome, id)

# Criando o objeto
f = Super_Filho('Beta', 0.3, 2020, 3 )

# Chamando a função 'mostrar'
f.mostrar()

# Criando o objeto
p = Super_Pai('Edcarlos', 0.1)

# Chamando o método 'mostrar'abs
p.mostrar()
print()

print('='*10, 'Herança com a função super()', '='*10)
class F_Super():
    def __init__(self, idade, sexo):
        self.i = idade
        self.s = sexo

    # Criando o método mostrar
    def mostrar(self):
        print(f'Sou o {self.i} e sou do sexo {self.s}.')

# Criando a classe filha
class F_Minimo(F_Super):
    def __init__(self, idade, sexo):
        self.fi = idade
        self.fs = sexo

        # herdando as propriedades da classe Pai(F_Super)
        super().__init__('Roger', 'M')

    # Criando o método mostrar da classe filha
    def mostrarF(self):
        print(f'Tenho {self.fi} e sou do sexo {self.fs}.')

# Criando o objeto filho
f = F_Minimo(28, 'M')

# Chamando o método mostrarF
f.mostrarF()

# Chamando a classe Pai pela função 'super()'
f.mostrar()
print()

print('x'*10, 'Heranças Múltiplas', 'x'*10)
class Hera1(object):
    def __init__(self):
        self.txt = 'Herança 1'
        print(f'Iniciado a {self.txt}.')

class Hera2(object):
    def __init__(self):
        self.tx = 'Herança 2'
        print(f'Iniciado a {self.tx}.')

class Mult(Hera1, Hera2):
    def __init__(self):
        # Chamando os construtores da 'Hera1' e 'Hera2'
        Hera1.__init__(self)
        Hera2.__init__(self)
        print('Heranças Multiplas')

    # Criando o método mostrar
    def mostrar(self):
        print(f'Mostrando a {self.txt} e a {self.tx}.')

# Criando o objeto da herança multipla
obj = Mult()

# Chamando o método mostrar
obj.mostrar()
print()

print('"'*10, 'Herança Multinível', '"'*10)
class Father(object):
    # Criando o construtor
    def __init__(self, nome):
        self.n = nome

    # Recebendo o nome
    def getName(self):
        return (f'Sou o {self.n}.')

# Herdando a classe Father
class Son(Father):
    # Criando o construtor
    def __init__(self, n, sobrenome):
        Father.__init__(self, n)
        self.sb = sobrenome

    # Recebendo o sobrenome
    def getSobNo(self):
        return (f'Meu sobrenome é {self.sb}.')

# Herdando a subclasse Son
class Grand_Son(Son):
    # Criando o Construtor
    def __init__(self, n, sb, cidade):
        Son.__init__(self, n, sb)
        self.cid = cidade

    # Recebendo a cidade
    def getCid(self):
        return (f'de(a) {self.cid}.')

# Criando o objeto Grand_Son
neto = Grand_Son('Pedrinho', 'herança', 'São Paulo')

# Mostrando o resultado
print(neto.getName(), neto.getSobNo(), neto.getCid())
