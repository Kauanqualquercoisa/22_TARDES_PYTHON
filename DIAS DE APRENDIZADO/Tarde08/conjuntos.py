""" 
Conjunto em Python são coleções assim como listas e tuplas,
a diferença é um eles não admitem elementos duplicados, o que
em alguns contextos pode ser bastante útil. Além disso, eles são 
mutáveis 

Os conjuntos são declarados utilizando chaves "{}" ou podem ser criados
utilizando o construtor set() que só admite como argumento iteráveis.

"""
# Exemplos de declaração e uso do set()

conjunto = {'Praia','areia','mar'}

# nesse exemplo o '2' e o '5' estão sendo repetidos na lista, ao usar o construtor set()
# a variável conjunto_2 vai armazenar os valores da lista excluindos as duplicações
 
conjunto_2 = set([1,2,2,2,2,3,4,5,5]) # {1,2,3,4,5}

print(conjunto_2)
