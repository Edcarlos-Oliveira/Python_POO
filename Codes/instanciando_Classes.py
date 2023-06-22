print ('*' * 10, 'Instanciando Classes', '*' * 10)

# Criando a classe
class Lapis:
    # Criando os atributos
    material = "Madeira"
    cor = "Preta"

    # Criando os métodos
    def saida(self):
        print(f'Eu tenho um lápis de {self.material} na cor {self.cor}')

# Instanciando o objeto        
resultado = Lapis()

# Saida por atributos
print(resultado.material)

# Saída pelo método
resultado.saida()
print()

print('-'*10, 'Trabalhando com autoparâmetros', '-'*10)
class Paramt:
    # Definindo os atributos
    def __init__(self, nome, empresa):
        self.nom = nome
        self.tra = empresa

    # Definindo os métodos
    def metds(self):
        print(f'Meu nome é {self.nom} e trabalho na Empresa {self.tra}.')

# Criando o objeto:
dados = Paramt('Edcarlos', 'NProdutos')

# Chamando o método
dados.metds()
print()

print('¨'*10, 'Variáveis de Instâncias com Construtor', '¨'*10)

class Caneta:
    # Variável da classe
    tipo = 'Caneta'

    #Iniciando o método
    def __init__(self, marca, cor):
        # Instanciando as variáveis
        self.m = marca
        self.c = cor

# Criando os objetos
material1 = Caneta('Bic', 'Azul')
material2 = Caneta('Compactor', 'Preta')

# Saída dos detalhes de 'material1'
print(f'Material1 é um(a) {material1.tipo} da marca {material1.m} e da cor {material1.c}')
print()
# Saída dos detalhes de 'material1'
print(f'Material2 é um(a) {material2.tipo} da marca {material2.m} e da cor {material2.c}')
print()
print(f'Acessando a váriavel usando o nome da classe: {Caneta.tipo}')
print()

print('&'*10, 'Usando os métodos get e set', '&'*10)

class Borracha:
    tipo = 'Borracha'

    # Iniciando o método construtor
    def __init__(self, marca):
        self.ma = marca

    # Adcionando uma instancia a variável(set)
    def setCor(self, cor):
        self.cor = cor

    # Recupera a instancia da variável(get)
    def getCor(self):
        return self.cor

# Criando o objeto
mat1 = Borracha('Mercurio')
mat1.setCor('Verde')
print(f'Uma {mat1.tipo} da marca {mat1.ma} na cor {mat1.getCor()}.')
print()

print('#'*10, 'Utilizando o método __str__', '#'*10)
# Utilizando o método '__str__'
class Mstr:
    def __init__(self, nome, material):
        self.n = nome
        self.mat = material

    def __str__(self):
        return (f'Eu tenho um {self.n} de {self.mat} niquelado.')

# Criando o objeto
obj = Mstr('clips', 'aço')
print(obj)



