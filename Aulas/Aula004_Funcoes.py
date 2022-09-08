# O principio de uma função é utilizar o def(), isso diz ao py que estou usando uma função. Sempre utilizar a identação

#Ex:

def imprime():
    print("esta é uma função")

imprime()
imprime()

# Uma função pode ter parametros
# Uma função pode ter retorno

# ex:

def potencia(n):
    return n * n

x = potencia(3)
print(x)

# Função com valor default
# Valor default = se não passar algum parametro para a função ele utiliza valor default
#Ex:

def intervalo (inic=1, fim=10):
    for inic in range (1,fim+1):
        print(inic)

intervalo(1,12)
intervalo()  # Nota-se que aqui não foi repassado valor, então conforme definido na função ele retorna o valor default, ou seja se eu omitir o parametro ele me retorna um valor da mesma forma


"""
Funções Padrão
"""

#abs = retorna valor absoluto
#max = retorna maior valor


"""
Modulos Nativos
"""

