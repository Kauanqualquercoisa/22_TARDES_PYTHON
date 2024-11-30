""" 
Assim como em Listas e Tuplas, conjuntos tem seus metodos que
facilitam a manipulação das variáveis desse tipo de estrutura.

"""
# Método add: add() funciona como o append, mas para conjuntos

conjunto = set()

conjunto.add(3)
conjunto.add(4)

conjunto # {3,4}

# Método discard: discard() funciona como o remove, mas para conjuntos

conjunto.discard(3)
conjunto # {4}