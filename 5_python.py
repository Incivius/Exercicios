# Construa um algoritmo que leia as variáveis C e N, respectivamente código e número de horas trabalhadas 
# de um operário. E calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. Quando o número de horas 
# exceder a 50 calcule o excesso de pagamento armazenando-o na variável E, caso contrário zerar tal variável. 
# A hora excedente de trabalho vale R$ 20,00. No final do processamento imprimir o salário total e o salário 
# excedente.

Código = []
horas_trab = []
lista = []

for código in range(7):
    funcionario_ = input('Qual o seu nome? ')
    Código.append(funcionario_)
    horas_=  float(input('Qual o número de horas trabalhadas? '))
    horas_trab.append(horas_)
    if horas_ > 50:
        horas_sem = 50 * 10
        horas_add = (horas_ - 50) * 20
    elif horas_ <= 50:
        horas_sem = horas_ * 10
        horas_add = 0
    salario_total = horas_sem + horas_add
    salario_ex = horas_add
    lista.extend([funcionario_ , salario_total])
    print (Código)
    print (horas_)
    print (horas_trab)
    print (f'Seu salario total ficou em: {salario_total}, com o adicional de horas execedidas no total de: {salario_ex}')
    print (lista)




