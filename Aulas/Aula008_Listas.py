# Formas d e criar listas
# Uma lista é um vetor onde cada posição esta um objeto. Este objeto pode ser de qualquer tipo, inclusive outra lista

lst1 = [1,2,3,4,5]
print(lst1)

# Podemos ter diversos tipos de dados em uma lista
lst2 = [1,2,3,"4",True]
print(lst2)

# Lista com outra lista na segunda posição
lst3 = [12,[1,2,3,4,5],"a"]
print(lst3)

# Criando uma lista com range
lst4 = list(range(0 ,10 + 1))
print(lst4)

# Lista com range regressivo, de 2 em 2
lst5 = list(range(10, 0, -2))
print(lst5)

# Descobrindo o tamanho da lista desejada, neste caso da lst5
print(len(lst5))

print(len(lst1))

# Imprimindo um resultado conforme busca no indice, no ex. abaixo o indice 0 da lst1 é o número 1
print(lst1[0])

# Indice 2 da lst3 é um str
print(lst3[2])

# Alterando o valor
lst3[2] = "xx"
print(lst3[2])

print()
# Percorrendo uma lista. Aqui percorre uma range de 0 até o cimprimento(len) da lst4. Depois faço a impressão a partir do elemento n (neste caso é o elemento 0) somando 1 = ou seja 0+1 = 1
for n in range(0, len(lst4)):
    print(lst4[n]+1)