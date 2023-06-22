print('|'*10, 'Polimorfismo em Python', '|'*10)
class Poli:
    def __init__(self):
        self.p = 'Polimorfismo Embutido'
        self.n = [10,20,30]

    # Recebendo o resultado
    def resultado(self):
        print(f'Aqui estou usando a função len() para strings: {len(self.p)}')
        print(f'Aqui estou usando a função len() para lista: {len(self.n)}')

# Criando os objetos
obj = Poli()

# Mostrando o resultado
obj.resultado()
print()

print('#'*10, 'Polimorfismo definido pelo usuário', '#'*10)
class PoliU:
    def __init__(self, n1=0, n2=0, n3=0):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    # Recebendo os dados
    def result(self):
        return (self.n1 + self.n2 + self.n3)

# Criando os objetos:
obj = PoliU(2,3)
obj2 = PoliU(2,3,4)
print(f'A soma do obj é igual a: {obj.result()}')
print(f'A soma do obj2 é igual a: {obj2.result()}')
print()

print('-'*10, 'Polimrfismo usando classes diferentes com funções iguais', '-'*10)
class Sao_Paulo:
    def capital(self):
        print('A capital de São Paulo é São Paulo.')

    def local(self):
        print('São Paulo está localizado na região Sudeste.')

    def popul(self):
        print('A população de São Paulo é de 46.024.937 habitantes em 2022.')

class Bahia:
    def capital(self):
        print('A capital da Bahia é Salvador.')

    def local(self):
        print('A Bahia está localizado na região Nordeste')

    def popul(self):
        print('A população da Bahia é de 14.659.023 habitantes em 2022.')

# Criando os objetos
objSP = Sao_Paulo()
objBA = Bahia()

# Mostrando os resultados com "for"
for state in (objSP, objBA):
    state.capital()
    state.local()
    state.popul()
print()

print('>'*10, 'Polimorfismo com Herança', '<'*10)
class Gato:
    def cor(self):
        print('Existe gatos de muitas cores.')

    def significado(self):
        print('As cores dos gatos falam muito sobre a personalidade deles.')

class Preto(Gato):
    def significado(self):
        print('Os gatos pretos são considerados introspectivo, tímido e tranquilo.')

class Branco(Gato):
    def significado(self):
        print('Os gatos brancos são considerados calmos e pensativos.')

# Criando os objetos
objG = Gato()
objP = Preto()
objB = Branco()

# Mostrando os resultados
objG.cor()
objG.significado()

objP.cor()
objP.significado()

objB.cor()
objB.significado()

    
