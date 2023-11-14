numero = int(input('Digite um Valor ?'))
resultado = numero %2
if resultado == 0:
    print('Seu número vai ser PAR '.format(numero))
else:
    print('Seu número vai ser IMPAR'.format(numero))