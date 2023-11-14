from datetime import date
ano=int(input('\033[2;33;40m Digite um ano que você quer analisar ?Coloque o 0 para analisar o ano atual ? \033[35m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano %100 !=0 or ano %400 == 0:
    print('Seu Ano {} é BISSEXTO!'.format(ano))
else:
    print('Seu Ano {} Não é BISEEXTO!'.format(ano))