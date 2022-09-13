import numpy as np

# Biblioteca muito utilizada para tratar dados

""" Criando uma matriz unidimensional"""

#() é um parametro do método array do numpy
#[] é o vetor de dados

matriz_uni = np.array([12,34,26,18,10])
print(matriz_uni)
print(type(matriz_uni))

"""
Criando uma array de tipo específico
Criando uma array como float de 64bits
"""

print()
matriz_float = np.array([1.4, 3.6, -5.1, 9.42, 4.999])
print(matriz_float)

print()
matriz_int_64 = matriz_float.astype(np.int32)
print(matriz_int_64)



