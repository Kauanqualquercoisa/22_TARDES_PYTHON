""" 
Existem métodos da classe set que são uma extensão das operações 
com conjuntos, esses métodos retornam valores Booleanos (TRUE OU FALSE). 
sendo eles:

issubset() - verifica se todos os elementos de um conjunto estão contidos em outro.

issuperset() - verifica se um conjunto contém todos os elementos de outro.

isdisjoint() - verifica se dois conjuntos não compartilham nenhum elemento.

"""

# issubset()

A = {1,2,3}
B = {1,2,3,4,5,6,7}

A.issubset(B) # True, pois A está todo contido em B

B.issubset(A) # False, pois B não está todo contido em A


# issuperset()

B.issubset(A) # True, pois A está contido em B

A.issubset(B) # False, pois B não está todo dentro de A

# isdisjoint()

A = {1, 2, 3}
B = {4, 5, 6}
C = {3, 4}

A.isdisjoint(B) # True, porque A e B não têm elementos em comum

A.isdisjoint(C) # False, porque A e C compartilham o elemento 3

