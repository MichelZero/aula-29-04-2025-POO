# autor: Michel
# data: 2025-04-29

# 1- gere tupla dinamicamente de tamanho 5, ,
# de tamanho aleatório entre 1 e 20;

#gera tupla dinamicamente
# Cria um range de 5 elementos e atribui à variável t1
t1 = range(5)
print(t1)  # Imprime o objeto range (não é uma tupla ainda)
print()

# Converte o range em uma tupla e atribui novamente à variável t1
t1 = tuple(range(5))
print(t1)  # Imprime a tupla gerada a partir do range

# Importa a função randint do módulo random para gerar números aleatórios
from random import randint

# Gera uma tupla dinamicamente com tamanho aleatório entre 1 e 20
t1 = tuple(range(randint(1, 20)))
print(t1)  # Imprime a tupla gerada dinamicamente