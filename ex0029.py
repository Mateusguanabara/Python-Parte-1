velocidade = float(input('Digite a Velocidade Do Véiculo ?'))
if velocidade > 80:
 print('MULTADO,Você Ultrapassou o limite de 80km/h')
 multa = (velocidade-80)*7
 print('Você deve pagar uma Multa De R${:.1f}'.format(multa))
print('Tenha um BOM DIA!,diriga com segurança! ')

