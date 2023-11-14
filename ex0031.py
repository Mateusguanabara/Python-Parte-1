distância=float(input('Digite Sua Distância Percorrida ?'))
print('Você está prestes a começar uma viagem em {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('O Preço dá sua Passagem Será De R${:.1f}'.format(preço))