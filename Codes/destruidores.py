print('=-'*10, 'Usando os Destruidores', '=-'*10)
# Exemplo de destruidores automáticos
class Exemplo:
    # Criando o exemplo
    def __init__(self):
        print('Exemplo Criado com sucesso!')

    # Deletando o construtor
    def __del__(self):
        print('Destruidor chamado, Exemplo deletado com sucesso!')

# Criando o objeto
obj = Exemplo()

# Deletando o objeto
del obj
print()

print('§'*10, 'Destruidor exemplo 2 chamado depois do fim do programa', '§'*10)
class Exemplo2:
    # Inicializando
    def __init__(self):
        print('Exemplo 2 criado com SUCESSO!')

    # Chamando o destruidor
    def __del__(self):
        print('Destruidor chamado com SUCESSO!')

# Criando o objeto
def criObj():
    print('Objeto criado com SUCESSO!')
    obj = Exemplo2()
    print('Função finalizada!')
    return obj

# Chamando a função 'criObj'
obj = criObj()
print('Finalizando o Programa...')

