""" 
As lista podem armazenar todos os tipos de objetos, 
e como a lista também é um objeto, podemos então,
armazenar outras lista dentro de uma lista. Chama-se isso
de lista aninhadas, com isso podemos criar estruturas
bidemensionais (tabelas).

Ao fazer isso, para acessar a informação precisamos
informar a linha e a coluna do elemento. Isso seria
o equivalente a uma matriz em Python.

"""
# exemplo de uma matriz de 3 linhas e 4 colunas

matriz = [                 
    [1,2,4,'a'],
    [5,6,7,'b'],
    [9,8,0,'c']
]

# acesso aos elementos:

print(matriz[0]) # acessa toda a linha 0

print(matriz[0][3]) # acessa o último elemento da linha 0

print(matriz[2][2]) # acessa o terceiro elemento da última linha

