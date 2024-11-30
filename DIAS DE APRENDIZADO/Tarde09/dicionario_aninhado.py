""" 
Um dicionário aninhado é um dicionário que contém outros dicionários como valores. 
Em outras palavras, cada chave pode armazenar não apenas valores simples 
(como strings ou números), mas também outro dicionário, criando uma estrutura hierárquica

Então tem uma variável do tipo dicionário que armazena outros dicionários como seus valores.
 
Os dicionários aninhados são extremamente úteis para representar estruturas de dados hierárquicas 
ou agrupadas. Suas principais vantagens incluem organização e flexibilidade
"""
# Exemplo de Dicionário Aninhado:

alunos = {
    "aluno1": {"nome": "João", "idade": 20, "curso": "Engenharia"},
    "aluno2": {"nome": "Maria", "idade": 22, "curso": "Medicina"},
    "aluno3": {"nome": "Pedro", "idade": 19, "curso": "Direito"}
}

# Nesse exemplo, o dicionário alunos contém três chaves (aluno1, aluno2, aluno3), 
# cada chave está associada a um dicionário que armazena informações detalhadas sobre o aluno.

""" 
Para acessar os valores de um dicionário aninhado é necessario indexar uma das chaves 
do dicionário maior e a chave do dicionário interno

"""
# Exemplo de Acesso

alunos['aluno2']['nome'] # Maria
alunos['aluno3']['curso'] # Direito

# Exemplo de atribuição

alunos['aluno4'] = {'nome':'Kauã','curso':"Programador"}

