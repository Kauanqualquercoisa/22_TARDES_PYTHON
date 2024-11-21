# Método count(): Ele conta quantas vezes um determinado elemento aparece em uma lista
# elemento é uma string, um número, um número float etc.

lista = [0,0,0,3,4,5,0,0,"Python"]

print(lista.count(0)) # aparece 5 vezes o elemento '0' na lista
print(lista.count('Python')) # o elemento 'Python' aparece 1 vez

# Método extend(): adiciona um elemento à lista mesclando tudo

lista.extend(["Vermelho",'AZUL','Laranja',0,0,9])
print(lista)

# Método index(): Retorna a posiço da primeira ocorrência de um elemento de uma lista

print(lista.index("Vermelho")) # posição 9
print(lista.index(0)) # posição 0

#Método remove(): Remove o elemento passado no parâmetro do método

lista.remove('Vermelho')
print(lista)

#Método sort(): Ordena a lista de char em ordem alfabética

lista3 = ['z','w','h','a']

lista3.sort()

print(lista3)