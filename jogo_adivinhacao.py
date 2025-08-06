import random
from random import randint
from time import sleep

RN = randint(0, 5)
jogo=int(input('Vamos jogar um jogo? Eu escolhi um numero de 0 a 5, tente adivinhar qual é!'))
print('Processando...')
sleep(1)
if jogo == RN:
    print('Acertou! Pensei extamente em {}!'.format(RN))
else:
    print('Errou! Eu pensei em {}!'.format(RN))


