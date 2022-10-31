
bimestre = 0
maior_nota = 0
menor_nota = 10
soma = 0


for i in range(4):
    bimestre += 1
    valor = (float(input(f'Qual a nota do {bimestre}º bimestre? ')))
    soma += valor
    if valor >= maior_nota:
        maior_nota = valor
    if valor <= menor_nota:
        menor_nota = valor   
media = (soma)/ 4
print ('A media desse aluno foi de: %.2f' %media)
print ('Sua maior nota foi: %.2f' %maior_nota)
print ('Sua menor nota foi: %.2f' %menor_nota)