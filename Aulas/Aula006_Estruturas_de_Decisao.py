nota = input("Insira uma nota: ")
nota = float(nota)

if nota >= 7:
    print("Aprovado")
    print("Parabéns")
elif nota >= 4 and nota <= 6:
    print("Exame")
else:
    print("Reprovado")