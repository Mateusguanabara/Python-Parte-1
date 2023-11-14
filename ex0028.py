from random import randint
from time import sleep
computador=randint(0,5)
print('-'*45)
print('Tente Adivinhar o número que foi digitado...')
print('-'*45)
jogador=int(input('Que número eu pensei ??'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! , Você Acertou !'.format(computador))
else:
    print('ERROU!,Pensei em um número {} é não no {}'.format(computador,jogador))
