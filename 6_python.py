# Construa um algoritmo que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques 
# cilíndricos de combustível, 
# em que são fornecidos a altura e o raio desse cilindro. Sabendo que:
# A lata de tinta custa R$ 50,00
# Cada lata contém 5 litros
# Cada litro de tinta pinta 3 metros quadrados
# Dados de saída: custo (C) e quantidade de latas cheias (QTDE)

# Ab= p.r²
# Al = 2p. r. h
# At= 2.Ab + Al ou At = 2(p.r²) + 2(p.r.h)
# área total = 2x área da base + área lateral

print ('Para que eu possa calacular o melhor custo beneficio, preciso saber de duas coisas:')
Altura = float(input('Qual a altura do tanque? '))
raio = float(input('Qual o raio do tanque? '))

base = 3.14 * (raio ** 2)
al = 2 * 3.14 * raio * Altura
area_total = (2 * base) + al

Lata = 50
litro_metro = ((area_total)//15)
valor_final = Lata * litro_metro

print ('Será necessario %.0f latas de tinta para pintar esse tanque' %litro_metro)
print ('O valor total por tanque é de: %d'%valor_final)
