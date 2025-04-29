# autor: Michel
# data: 2025-04-29


#2 - verifique se um determinado elemento 
# esta contido na tupla ('a','b',1,2,'c',3,4,'d',5) 

# Você pode usar o operador in para verificar 
# se um determinado elemento está contido em uma tupla. 

tupla = ('a','b',1,2,'c',3,4,'d',5)
# elemento = 'c'
entrada = input("número ou string: ")
if entrada.isdigit():
  elemento2 = int(entrada)
else:
  elemento2 = entrada

if elemento2 in tupla:
    print(f'{elemento2} está contido na tupla')
else:
    print(f'{elemento2} não está contido na tupla')


# Você também pode usar o método count() para 
# verificar a frequência de um determinado elemento 
# na tupla, se o resultado for maior que zero, 
# significa que o elemento está contido na tupla.

tupla = ('a','b',1,2,'c',3,4,'d',5)
elemento = '6'

if tupla.count(elemento)>0:
    print(f'{elemento} está contido na tupla')
else:
    print(f'{elemento} não está contido na tupla')

