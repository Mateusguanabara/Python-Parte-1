import math
ângulo=float(input('Digite um ângulo que vc deseja ?'))
seno=math.sin((math.radians(ângulo)))
print('O ângulo de {} tem Seno de {:.2f}'.format(ângulo,seno))
cosseno=math.cos(math.radians(ângulo))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ângulo,cosseno))
Tangente=math.tan(math.radians(ângulo))
print('O ângulo de {} tem o Tangete de {:.2f}'.format(ângulo,Tangente))


