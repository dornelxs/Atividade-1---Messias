notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
