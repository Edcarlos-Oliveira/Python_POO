print('#'*10, 'Construtores Padrão', '#'*10)
class ConPad:
    def __init__(self):
        self.p = str(input('Qual seu nome? '))

    # Criando o método
    def print_P(self):
        print(f'Olá {self.p} esse é um construtor padrão.')

# Criando o objeto
obj = ConPad()

# Instanciando o método
obj.print_P()
print()

print('x'*10, 'Construtores Parametizado', 'x'*10)
class Dados:
    n1 = 0
    n2 = 0
    soma = 0

    # Definindo o Construtor
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    # Método para mostrar
    def mostrar(self):
        print(f'Primeiro número digitado foi {self.n1}.')
        print(f'Segundo número digitado foi {self.n2}')
        print(f'A soma de {self.n1} + {self.n2} = {self.soma}')

    # Método para somar os valores digitados
    def somar(self):
        self.soma = self.n1 + self.n2

# Criando os objetos
obj = Dados(int(input('Digite um valor: ')), int(input('Digite outro Valor: ')))

# Chamando o método somar
obj.somar()

# Mostrando o resultado
obj.mostrar()
print()

print('*'*10, 'Construtores Padrão e Parametizados', '*'*10)
class Con_Pad_Par:
    def __init__(self, nome=None):
        if nome is None:
            print('Construtor padrão chamado!')
        else:
            self.n = nome
            print(f'Construtor parametizado chamado com o nome de: {self.n}')

    # Criando o método com 'hasattr (função que verifica se um objeto tem algum atributo nomeado)'
    def temDados(self):
        if hasattr(self, 'n'):
            print(f'Dados passado com o nome de: {self.n}.')
        else:
            print('Dados sem nenhum nome!')

# Criando objeto do construtor padrão
objPd = Con_Pad_Par()

# Chamando o método
objPd.temDados()

# Criando objeto construtor parametizado
objPar = Con_Pad_Par('Edcarlos')

# Chamando o método
objPar.temDados()

