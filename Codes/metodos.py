print('-'*10, 'Métodos de Classes e Estáticos', '-'*10)
class Met_Class:
    def __init__(self, valor):
        self.v = valor

    def saida(self):
        return (f'Aqui está a saída do método de classe: {self.v}')

# Criando o objeto
obj = Met_Class(10)

# Mostrando o resultado
print(obj.saida())
print()

print('<'*10, 'Método Estático', '<'*10)
class Met_Est:
    def __init__(self, valor):
        self.vl = valor

    @staticmethod
    def mostrar(n1, n2):
        return max(n1, n2)

# Criando o objeto
objeto = Met_Est(10)

# Mostrando os resultados
print(f'Mostrando o maior valor: {Met_Est.mostrar(20,30)}')
print()
print(f'Mostrando o maior valor pelo [objeto]: {objeto.mostrar(20,30)}')
print()

print('><'*10, 'Implementação completa com os dois métodos', '><'*10)
from datetime import date 
class Cachorro:
    def __init__(self, cor, idade):
        self.c = cor
        self.i = idade

    # Criando o método de classe
    @classmethod
    def verif(stt, cor, idade):
        return stt(cor, date.today().year - idade)

    # Criando o método estatico
    @staticmethod
    def adulto(idade):
        if idade < 7:
            return (f'Com {idade} está na fase adulta!')
        else:
            return (f'Com {idade} não está na fase adulta!')

# Criando os objetos
ch1 = Cachorro('Branco', 11)
ch2 = Cachorro.verif('Preto', 2020)

# Mostrando os resultados
print(f'O cachorro {ch1.c} tem {ch1.i} anos de idade.')
print(f'O cachorro {ch2.c} tem {ch2.i} anos de idade.')

# Verificando se é adulto
print(Cachorro.adulto(5))
