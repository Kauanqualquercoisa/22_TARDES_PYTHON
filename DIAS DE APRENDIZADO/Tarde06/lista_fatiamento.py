""" 
Os elementos contidos na lista podem ser acessados
utilizando o fatiamento, isso é útil para resolver
problemas em que é preciso manipular as strings  
principalmente.

"""
# exemplo de fatiamentos

lista = ['p','y','t','h','o','n']

lista[2:] # imprime t,h,o,n
lista[1:4] # imprime y,t,h,o
lista[::2] # imprime p,h
lista[0:5:1] # imprime p,t,o

# espelhamento de uma string:

lista[::-1] #imprime o,n,h,t,y,p

""" 
Exercício prático: Desenvolva um programa em Python que leia do usuário
duas strings e verifique se elas são palíndromas mútuas, ou seja, se
uma é igual à outra quando lida de traz para frente.

"""
string_1 = list(input("String 1: "))
string_2 = list(input("String 2: "))

palindromo = string_1

palindromo = palindromo[::-1]

if string_2 == palindromo:
    print("São palíndrmos mútuos")
else:
    print("Não são palíndromos mútuos")