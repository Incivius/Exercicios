# Construa um algoritmo que calcule a média aritmética entre quatro notas bimestrais quaisquer fornecidas por um aluno (usuário).

avaliações = 1
legendas = 1
bimestre = []
while avaliações <= 4:
    notas = float(input(f'Insira o valor da nota do aluno no {legendas}º Bimestre: '))
    bimestre.append (notas)
    avaliações += 1
    legendas += 1

media = sum(bimestre)/ len (bimestre)
print (f'A média do aluno foi de: {media}')