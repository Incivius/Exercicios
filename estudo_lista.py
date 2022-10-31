lista = ['Caju', 'Laranja', 'Banana', 'Uva','Abacate','Manga', 'Azul']

for frutas in lista:
    print (frutas)

lista [0] = 'Morango'

for frutas in lista:
    print (frutas)

lista.remove('Morango')
for frutas in lista:
    print (frutas)

del lista[0]

for frutas in lista:
    print (frutas)

lista.sort()
for frutas in lista:
    print (frutas)

lista.reverse()
for frutas in lista:
    print (frutas)

for i, p in enumerate(lista):
    print(i + 1, '=>', p)

# soma = sum(lista)
# print (soma)

lista.extend(['---------','uva'])
print (lista)

for frutas in lista:
    print (frutas)

lista.count('Maça')
lista.index('Banana')
lista.insert(1, 'Casa')

print (lista)

lista.pop(0)
print (lista)

horas = '23/06/2001'.split('/')
print (horas)


# [x**2 for x in lista if x%2 == 0]
# [i for i in lista if i>5]

teste = [9]* 4
teste = teste + [1]*3
print(teste)

teste2 = list('Formiga')
teste2[2]= ' '
''.join(teste2)

print(''.join(teste2))
teste2.sort(reverse = True)
print (''.join(teste2))

#------------------------------------------

Exer = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
exercicio2 = []
for i in Exer:
    if i >= 1 and i <= 9:
        exercicio2.append(i)

print (exercicio2)

exercicio2 = []
for i in Exer:
    if i >= 8 and i <= 13:
        exercicio2.append(i)

print (exercicio2)

exercicio2 = []
for i in Exer:
    if i%2 == 0:
        exercicio2.append((i-1)+2)

print (exercicio2)

exercicio2 = []
for i in Exer:
    if i%2 == 0 or i%3 == 0 or i%4 == 0:
        exercicio2.append(i)

print (exercicio2)


lista = ['Caju', 'Laranja', 'Banana', 'Uva','Abacate','Manga', 'Azul']
lista.sort(reverse = True)

print(lista)



