import math
cttoposto=float(input('O comprimento do Cateto Oposto:'))
cttadjacente=float(input("O Comprimento do Cateto Adjacente de um triângulo Retângulo:"))
calcule=(cttoposto ** 2 + cttadjacente ** 2) **(1/2)
print('A Hipotenusa dos Catetos é: {:.1f} cm'.format(calcule))
