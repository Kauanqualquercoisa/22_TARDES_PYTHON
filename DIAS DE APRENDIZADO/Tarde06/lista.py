""" 
Em Python as lista é semelhante aos vetores em C,
que aqui são chamadas de objetos, os elementos de uma
lista precisam estar dentro dos colchetes "[]" 

"""

# formas de declarar uma lista

frutas = ['banana','maça','mamão','goiaba']

lista = [] # exemplo de lista vazia

'''
CONSTRUTOR "list()" ele transforma o elemento dentro do parâmetro em um interável
Ou seja, "Python" que é o parâmetro será convertido para uma lista onde cada letra tem uma posição
Por exemplo a partir de agora letras[0] = "P" 
'''
letras = list("Python") 

print(letras[0])

# outro exemplo de uso do construtor list()

numeros = list(range(10)) # vai criar uma lista com numero de 0 a 9

print(numeros)
