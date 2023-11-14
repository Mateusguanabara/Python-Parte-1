print('-_-' *20)
print('Segmento Dos Triângulos')
print('-_-'*20)
r1=float(input('Digite o 1º Segmento:'))
r2=float(input('Digite o 2º Segmento:'))
r3=float(input('Digite o 3º Segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos Acima Podem Formar Um TRIÂNGULO!')
else:
    print('Os Segmentos Acima Não Podem Formar Um TRIÂNGULO!')

