"""  
Conjuntos, assim como na matemática, podem ser usados para realizar
operações como união, intersecção, dferença, etc.

Sendo esses os métodos dessa estrutura

"""
# Método União: union()

conjunto_a = {1,2,3}
conjunto_b = {4,5,6}

conjunto_a.union(conjunto_b) # {1,2,3,4,5,6}

# Método Intersecção: intersection()

conjunto_a = {2,4,5,6}
conjunto_b = {4,2,8,6}

conjunto_a.intersection(conjunto_b) # {2,4,6}

# Método Diferença: difference()

conjunto_a.difference(conjunto_b) # {5}
conjunto_b.difference(conjunto_a) # {8}

# Diferença Simétrica: symmetric_difference()

conjunto_a.symmetric_difference(conjunto_b) # {5,8}