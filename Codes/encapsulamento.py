print('<'*10, 'Exemplo de Encapsulamentos', '>'*10)
print('PROTEGIDOS:')
class Protect:
    # Criando o construtor
    def __init__(self):
        self._a = 2      # Variável '_a' protegida

# Derivando a classe protect
class Deriv(Protect):
    # Criando o construtor
    def __init__(self):
        # Chamando o construtor da classe protect
        Protect.__init__(self)
        print(f'Sou a variável protegida da classe Protect: {self._a}')

        # Modificando a variável protegida
        self._a = 3
        print(f'Sou a variável protegida modificada fora da classe: {self._a} ')

# Criando os objetos
obj = Deriv()
obj1 = Protect()

# Mostrando o 'obj'
print(f'Acessando a variável protegida da classe Deriv: {obj._a}.')

# Mostrando o 'obj1'
print(f'Acessando a variável protegida da classe Protect: {obj1._a}')
print
print()

print('/'*10, 'Variáveis Privadas com Encapsulamento', '/'*10)
class Private:
    # Criando o método construtor
    def __init__(self):
        # Definindo as variáveis privadas (private)
        self.b = 'Edcarlos'  
        self.__c = 'Oliveira' # Nesse caso consegue ser chamada só dentro da classe Private
        
# Derivando a classe Private
class DerivP(Private):
    # Construtor
    def __init__(self):
        # Chamando o construtor da classe Privada
        Private.__init__(self)
        print(f'Sou a variável da classe Private: {self.__c}') # Vai apresentar erro

# Criando os objetos
objeto = Private()

# Mostrando o resultado
print(f'Eu sou a variável não protegida: {objeto.b} {self.__c}.')

