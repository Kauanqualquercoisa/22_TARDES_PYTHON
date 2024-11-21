"""" 
Em Python existem vários métodos que servem para manipular ou interagir com os elementos da classe
ou então realizar operações específicas relacionadas ao objeto. São como funções já prontas para
serem utilizadas.

"""
# MÉTODO append(): Serve para atribuir um elemento (está dentro do parâmetro) dentro de um objeto:

lista = [] 

lista.append(1)
lista.append("Kauã")
lista.append(560.55)

print(f"método append(): {lista}") 

# MÉTODO clear(): Limpa a lista tornando ela uma lista vazia

lista.clear()

print(f"\nlista vazia pelo método clear(): {lista}")

# Método copy(): Faz uma cópia da lista em outro endereço de memória

lista = [1,2.3,'Python',78,99] 

lista2 = lista.copy()

print(f"\nLista 1: {lista} \nLista 2: {lista2}") # tem o mesmo conteúdo, mas em endereços diferentes

print(f"\nEndereço de Lista 1: {id(lista)} \nEndereço de Lista 2: {id(lista2)}")