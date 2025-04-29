# autor: Michel
# data: 2025-04-29


#2 - verifique se um determinado elemento 
# esta contido na tupla ('a','b',1,2,'c',3,4,'d',5) 

# Você pode usar o operador in para verificar 
# se um determinado elemento está contido em uma tupla. 



# Define uma tupla contendo elementos de diferentes tipos (strings e inteiros)
tupla = ('a', 'b', 1, 2, 'c', 3, 4, 'd', 5)

# Comentário desnecessário, pois a variável 'elemento' não está sendo usada
# elemento = 'c'

# Solicita ao usuário que insira um valor (pode ser um número ou uma string)
entrada = input("número ou string: ")

# Verifica se a entrada do usuário é composta apenas por dígitos (ou seja, é um número)
if entrada.isdigit():
    # Converte a entrada para um número inteiro, caso seja um número
    elemento2 = int(entrada)
else:
    # Caso contrário, mantém a entrada como string
    elemento2 = entrada

# Verifica se o valor fornecido pelo usuário está presente na tupla
if elemento2 in tupla:
    # Se estiver, imprime uma mensagem indicando que o valor está contido na tupla
    print(f'{elemento2} está contido na tupla')
else:
    # Caso contrário, imprime uma mensagem indicando que o valor não está na tupla
    print(f'{elemento2} não está contido na tupla')


# Você também pode usar o método count() para 
# verificar a frequência de um determinado elemento 
# na tupla, se o resultado for maior que zero, 
# significa que o elemento está contido na tupla.

# Define novamente a mesma tupla já declarada anteriormente, o que é redundante
tupla = ('a', 'b', 1, 2, 'c', 3, 4, 'd', 5)

# Define um elemento fixo ('6') para verificar se está contido na tupla
elemento = '6'

# Usa o método count() para verificar a frequência do elemento na tupla
if tupla.count(elemento) > 0:
  # Se o elemento estiver presente, imprime que está contido na tupla
  print(f'{elemento} está contido na tupla')
else:
  # Caso contrário, imprime que não está contido na tupla
  print(f'{elemento} não está contido na tupla')

