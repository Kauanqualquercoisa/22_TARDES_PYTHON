"""  

Em Python existe operadores de identidade que são:
"is" e "is not". Servem para comparar se uma variavel
ocupa o mesmo espaço de memória que a outra.


"""

x= [1,2,3]
y = x
a = [1,2,3]

print(x is y)
print(x is not y)
print(x is a)

""" 
Acima, por mais que x tenha o mesmo conteúdo de a 
x is a é false, pois em python as listas são consideradas
objetos diferentes
"""

x = "Olá"
y = x
a = "Olá"

print(x is y)
print(x is not y)
print(x is a)