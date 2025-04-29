# autor: Michel
# data: 2025-04-29

# 1- gere tupla dinamicamente de tamanho 5, ,
# de tamanho aleatório entre 1 e 20;

#gera tupla dinamicamente
t1 = range(5)
print(t1)
print()
t1 = tuple(range(5))
print(t1)

#importar a função randint
from random import randint

t1 = tuple(range(randint(1,20)))
print(t1)