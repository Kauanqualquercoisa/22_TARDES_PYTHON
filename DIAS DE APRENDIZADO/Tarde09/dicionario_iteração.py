""" 
Existem duas formas de iteração de um dicionário em Python
"""

alunos = {
    "aluno1": {"nome": "João", "idade": 20, "curso": "Engenharia"},
    "aluno2": {"nome": "Maria", "idade": 22, "curso": "Medicina"},
    "aluno3": {"nome": "Pedro", "idade": 19, "curso": "Direito"}
}

# Primeira forma

for chave in alunos:
    print(chave,alunos[chave]) 
    
# print(chave) - Imprime a variável chave que está recebendo apenas o valor da chave. ex: aluno1,aluno2,aluno3
# print(alunos[chave]) - Imprime os pares chave-valor das chaves internas.

# Segundo Forma: Usando o método items()

for chave,par_chave_valor in alunos.items():
    print(chave,par_chave_valor)
    
# o método items() é responsável por fazer a mesma coisa da primeira forma, só de maneira mais direta