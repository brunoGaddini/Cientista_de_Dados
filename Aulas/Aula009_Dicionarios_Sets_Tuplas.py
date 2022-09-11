# Dicionários: estruturas Chave/Valor
# Essa estrutura é muito comum em ciência de dados
# A chave e o Valor estão sempre relacionados
# A separação da chave e valor é feita pelo :

Notas = {'João': 6.0, 'Maria': 8.0, 'Bruno': 9.0}
print(Notas)

print()
# Imprimindo uma chave específica
print(Notas['João'])

# Para saber todas as chaves que existe no meu dicionário
print(Notas.keys())

# Para saber todos os valores existentes no meu dicionário
print(Notas.values())

# Testar logicamente a existência. Retorna um valor lógico
print('João' in Notas)
print('Fernando' in Notas)

print()
# Deletando um elemento
del Notas['João']
print(Notas)

print()
# Adicionando um elemento
Notas['Ana'] = 9.0
print(Notas)

print()
# Busca um valor, se não for encontrado, imprime um segundo parâmetro
print(Notas.get('Geraldo', "Aluno não cadastrado!"))

# Agora teste com um valor existente
print()
print("Agora testando com um valor existente")
print(Notas.get('Ana', "Aluno não cadastrado!"))

# Sets são conjuntos não ordenados de elementos não repetidos
# Possui estrutura semelhante ao dicionário
# Se o elemento não estiver repetido ele inclui

print()
set_bigdata = {'Spark', 'Hive', 'Sqoop'}
print(set_bigdata)

# Verifica a existência
print()
print('Spark' in set_bigdata)

print()
# Adicionando elemento
set_bigdata.add('Hadoop')
print(set_bigdata)

print()
print("Número de elementos", len(set_bigdata))

# Tentnado imprimir um valor repetido, nota-se que um set só retorna elementos distintos
set_bigdata.add("Spark")
print(set_bigdata)

# Tuplas são listas que não podem ser alteradas
# Listas usam [], tuplas usam ()

print()
tupla = (1,2,3,4,5,6,7)
print(tupla)

print()
# Retornando um valor conforme busca por indice
print(tupla[4])

# Dicionários em que cada posição recebe uma tupla
print()
dic_tuplas = {(0,1): 0, (1,2): 1, (2,3): 2, (3,4): 3, (4,5): 4, (5,6): 5, (6,7): 6, (7,8): 7, (8,9): 8, (9,10): 9}
print(dic_tuplas)

print()
print(type(Notas))
print(type(set_bigdata))
print(type(dic_tuplas))







