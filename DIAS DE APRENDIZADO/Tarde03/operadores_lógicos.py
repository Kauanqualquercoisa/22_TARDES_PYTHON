saldo = 200
saque = 100
limite = 200

print(saldo<saque and saldo == limite) # false
print(saldo>saque and saldo == limite) # True

print(saldo<saque or saldo != limite) # false

z = saldo<saque or saldo != limite
print(not z)

""" 
Em Python uma string vazia recebe o valor False
e uma lista vazia também recebe esse valor

"""

lista = []
print(not lista) # negando o false você obtém o True]

string = ""
print(not string)
string = "conteudo"
print(not string) # False pois nega o True