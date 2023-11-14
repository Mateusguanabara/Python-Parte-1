print('-_-'*10)
print('Desafio 36')
print('-_-'*10)
Casa=float(input('Digite o valor da Casa?'))
Salário=float(input('Digite o Seu Sálario?'))
Anos=float(input('Quantos Anos Ele Vai Pagar Essa Casa?'))
minímo = Salário * 30/100
prestação = Casa / (Anos * 12)
print('Para Pagar uma Casa de R${:.2f} em {:.2f} Anos'.format(Casa,Anos))
print('A Prestação Será De R${:.2f}'.format(prestação))
if prestação <= minímo:
  print('Sua Prestação Está , APROVADA!!! \n PARÁBENS')
else:
  print('Seu Empréstimo Não Foi , CONCEDIDO!! \n TENTE DENTRO DE 30 DIAS!!')





