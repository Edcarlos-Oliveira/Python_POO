print('>'*10, 'Variáveis Estáticas ou de Classes', '>'*10)
class Var_Class:
    vc = 'Edcarlos'                     # Variável de classe
    def __init__(self, txt, valor):
        self.t = txt                    # Variável de Instancia
        self.v = valor                  # Variável de Instancia

# Criando os objetos
a = Var_Class('Oliveira', 10)
b = Var_Class('Estudante', 1000)

# Mostrando os resultado
print(f'Mostrando a variável de classe: {a.vc}')
print(f'Mostrando a variável de classe pelo objeto b: {b.vc}')
print()
print(f'Mostrando a variável de instancia, objeto a: {a.t}')
print(f'Mostrando a variável de instancia, objeto b: {b.t}')
print(f'Mostrando a variável de instancia, objeto a: {a.v}')
print(f'Mostrando a variável de instancia, objeto b: {b.v}')
print()

# Alterando apenas o objeto 'a', nesse caso 'b' permanece com os dados anteriores
a.vc = 'Lima'
print(f'Objeto [a] alterado para: {a.vc} ')
print()
# Alterando todas instancias da classe
Var_Class.vc = 100
print(f'Mostrando o objeto [a]: {a.vc}')
print(f'Mostrando o objeto [b]: {b.vc}')
print()

print('<'*10, 'Classe Estática', '>'*10)
class Estat:
    static = 10                             # Variável estatica
    def __init__(self):
        Estat.static -= 1
        self.iv = Estat.static              # Variável Instanciada

# Criando os objetos
obj = Estat()

# Mostrando o resultado
print(f'O novo valor do [obj] chmando a instancia é igual a: {obj.iv}')

obj1 = Estat()
print(f'Valor do [obj1] chamando a instancia: {obj1.iv}')
print(f'O novo valor chamando a classe é igual a: {Estat.static}')
print()



