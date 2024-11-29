""" 
As Tuplas são "irmãs" das listas, mas diferente das listas, as tuplas 
não podem ser alteradas, ou seja, são imutáveis. Além disso, sua declaração
em Python é feita de forma diferente das listas.

Os construtures das tuplas são tuple(), com isso podemos fazer a conversão.

"""

# Exemplos:

frutas = ('laranja','maça','banana',)

nome = tuple("Kauã") # convertendo a string "Kauã" para uma tupla = ('k','a','u','ã',)

numeros = tuple([1,2,3,54,5]) # convertendo a lista com inteiros para um tupla com inteiros.

''' 
OBS: As tuplas são declaradas com parenteses "()" e como parentes
em Python já são usados para precedência de operações, pode haver casos,
dependendo da situação, em que o interpretador se confuda e não identifique 
a tupla declarada, por isso é recomendado adicionar uma vírgula ',' no final
das tupla para indicar para o interpretador que é sim uma tupla

'''
# Exemplo de declaração de tupla:

país = ('Brasil',) # tupla com um único elemento e com a vírgula no final
idade = (18,)  # tupla com um único elemento e com a vírgula no final

# exemplo prático: Caso você queira concatenar duas tuplas usando o "+"

n1 = (18) + (13) # SEM a vírgula você está soma 18 com 13

n2 = (18,)+(13,) # COM a vírgula você está concatenando duas tuplas, ficando n2 = (18,13)

print(f'n1: {n1}\nn2: {n2}')