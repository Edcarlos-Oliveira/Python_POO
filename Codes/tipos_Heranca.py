print('=-'*10, 'Tipos de Herança', '=-'*10)
print('Herança de Hierarquia.')
class Hier:    
    # Método da classe Pai
    def hier1(self):
        print('Essa função está na classe HIER(Pai).')

# Criando a classe filho1
class Filho1(Hier):
    # Método da classe filho1
    def hier2(self):
        print('Essa função está em filho1.')

# Criando a classe filho2
class Filho2(Hier):
    # Método da classe filho2
    def hier3(self):
        print('Essa função está em Filho2')

# Criando os objetos
obj1 = Filho1()
obj2 = Filho2() 

# Chamando o tipo de herança
obj1.hier1()
obj1.hier2()
print()
obj2.hier1()
obj2.hier3()
print()

print('='*10, 'Herança Hibrida', '='*10)
class Casa:
    def primeiro(self):
        print('Essa função está em Casa.')

class Morador1(Casa):
    def segundo(self):
        print('Essa função está em Morador 1.')

class Morador2(Casa):
    def terceiro(self):
        print('Essa função está em Morador 2.')

class Morador3(Morador1, Morador2):
    def quarto(self):
        print('Essa função está em Morador 3')

# Criando o objeto
obj = Morador3()

# Mostrando o resultado
obj.primeiro()
obj.segundo()
obj.terceiro()
obj.quarto()
