# autor: Michel
# data: 2025-04-29

# 3- Dada uma tupla de nomes de alunos e 
# suas respectivas notas, 
# escreva um programa que
# imprima o nome do aluno com a maior 
# nota e o nome do aluno com a menor nota.

# Inicializa a tupla de alunos com seus respectivos nomes e notas
alunos = (("João", 8.5), ("Maria", 9.2), ("José", 7.1), ("Ana", 8.7), ("Carlos", 6.5))

# Define variáveis para armazenar a maior e menor nota, e os nomes correspondentes
maior_nota = 0  # Inicialmente, a maior nota é 0
menor_nota = 10  # Inicialmente, a menor nota é 10
maior_nome = ""  # Inicialmente, o nome do aluno com a maior nota é vazio
menor_nome = ""  # Inicialmente, o nome do aluno com a menor nota é vazio

# Itera sobre a tupla de alunos para encontrar a maior e menor nota
for nome, nota in alunos:
    if nota > maior_nota:  # Verifica se a nota atual é maior que a maior nota encontrada
        maior_nota = nota  # Atualiza a maior nota
        maior_nome = nome  # Atualiza o nome do aluno com a maior nota
    if nota < menor_nota:  # Verifica se a nota atual é menor que a menor nota encontrada
        menor_nota = nota  # Atualiza a menor nota
        menor_nome = nome  # Atualiza o nome do aluno com a menor nota

# Exibe o aluno com a maior nota e a menor nota
print("O aluno com a maior nota é", maior_nome, "com nota", maior_nota)
print("O aluno com a menor nota é", menor_nome, "com nota", menor_nota)



