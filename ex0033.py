a=int(input('\033[31mDigite um valor ?\033[m'))
b=int(input('\033[32mDigite outro valor ?\033[m'))
c=int(input('\033[33mDigite último valor ?\033[m'))
#Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é maior
    maior=a
if b>a and b>c:
        maior=b
if c>a and c>b:
        maior=c
print('\033[1;37;40mMenor valor Digitado foi {}\033[m'.format(menor))
print('\033[7;37;40mMaior valor Digitado foi {}\033[m'.format(maior))
