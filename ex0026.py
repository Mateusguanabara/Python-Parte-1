letra=str(input('digite uma frase ?')).upper().strip()
print('A Letra A aparece {} Vezes na Frase'.format(letra.count('A')))
print('A Primeira Letra A apareceu na posição {}'.format(letra.find('A')+1))
print('A última letra A apareceu na posição {}'.format(letra.rfind('A')+1))



