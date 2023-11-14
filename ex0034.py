salário = (float(input('Digite o Valor Do Seu Salário ?R$')))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
    print('Você Recebia Esse Valor R${} Com o Aumento Foi Para R${}'.format(salário,novo))














