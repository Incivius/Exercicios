# Construa um algoritmo para calcular o volume de uma esfera de raio R, em que R é um dado fornecido pelo usuário.
#  Forneça como saída o resultado do cálculo executado.

raio = float(input('Qual o tamanho do Raio da esfera? '))
cubo = raio ** 3
constante = 4/3 *3.14
V = 4/3 * 3.14 * (raio**3)
print ('Para calcular o Volume de um esfera usaremos a seguinte formula: Volume = 4/3 πr³')
print ('Trazendo essa formula para a nossa operação, ficará assim: Volume = 4/3 * 3.14 * (raio**3)')
print ('(π) é a proporção numérica definida pela relação entre o perímetro de uma circunferência e seu diâmetro')
print ('(raio) é o valor que você definiu acima, resultando na seguinte operação: ')
print (f'Volume = 4/3 * 3.14 * ({raio} ** 3)')
print (f'Volume = 4/3 * 3.14 * ({cubo})')
print (f'Volume = {constante} * ({cubo})')
print (f'Volume = {V}')

