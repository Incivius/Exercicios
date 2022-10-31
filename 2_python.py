# Construa um algoritmo que, tendo como dados de entrada dois 
# pontos quaisquer do plano, P(x,y)  e Q(x,y), imprima o resultado do cálculo da distância entre eles.
coletas = 1
listaX = []
listaY = []

while coletas <= 2:
    if coletas == 1:
        Px = int(input('Qual a posicão em x do ponto P? '))
        Qx = int(input('Qual a posicão em x do ponto Q? '))
        listaX.append(Px)
        listaX.append(Qx)
        coletas += 1
    elif coletas == 2:
        Py = int(input('Qual a posicão em y do ponto P? '))
        Qy = int(input('Qual a posicão em y do ponto Q? '))
        listaY.append(Py)
        listaY.append(Qy)
        coletas += 1

distancia = (((listaX[1] - listaX[0])**2)+((listaY[1]-listaY[0]**2)))**0.5
print (f'A distancia entre os pontos é de: {distancia}')