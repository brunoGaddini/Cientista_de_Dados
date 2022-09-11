#Exemplo com while

count = 1
while count <= 5:
    print(count)
    count += 1

print()
# Exemplo com for
# Possui inicio, parada, incremento
# O incremento é opcional
# O incremento pode ser negativo

# No primeiro exemplo o contador da range não se inicia no 0
for n in range(0,10):
    print(n+1)

print()
for n in range(0,11):
    print(n)

# Exemplo de contagem inversa pulando de 2 em 2 (-2)
print()
for n in range(10,0,-2):
    print(n)

# O break faz com que o laço pare completamente
print()
for n in range(0, 20):
    if n == 4:
        break
    print(n)

# O continue não interrompe a excução do laço, ele pula conforme a condicional e depois continua a leitura do laço
print()
for n in range(0, 10):
    if n == 4:
        continue
    print(n)

