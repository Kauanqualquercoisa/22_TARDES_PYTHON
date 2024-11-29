""" 
Tuplas aninhadas funcionam da mesmas forma das listas aninhadas,
representam as matrizes em python, mas com a diferença de que 
não podem ser alteradas, pois como já sabemos são imutáveis.

"""

matriz_tupla = (

(1,'a','b',)
(2,'c','d',)
(3,'e','f',)
)

# assim como em Listas para acessaar os elemntos precisamos informar a linha e a coluna

matriz_tupla[0][2] # 'b'
matriz_tupla[1][2] # 'c'
matriz_tupla[0] # (1,'a','b')

