""" 
Em Python existe operadores de associação que fazem
a verificação de se uma valor está contido em uma 
lista, string, enfim em uma sequência qualquer ou até 
dicionário e conjunto de dados.

"""

lista = [2,4,56,2,54,3,54,7,5]
palavra = "introdução a python está d+"
vogais = ['A','E','I','O','U']

print("python" in palavra)
print("ntrodução" in palavra)
print(54 not in lista) # False pois é a negação da associaçaõ
print("I" in vogais) 