"""
Em Python usa-se construtores para
converter variáveis de um tipo para outro
    
"""
idade = 19
preço = 10.8

print(idade,preço)
tipo1, tipo2 = type(preço), type(idade)
print(f"Preço: {tipo1}, idade : {tipo2}")


idade = float(idade)

preço = int(preço)
print(preço,idade)# Isso fez com que idade passasse a ter .0 

tipo1, tipo2 = type(preço), type(idade)
print(f"Preço: {tipo1}, idade : {tipo2}")

#OBS: Para o interpretador retornar o tipo de uma uma variavel usa-se a função type(nome_variavel)


""" 
Para usar os construtores que convertem um tipo para outro
basta colocar o nome do tipo e abrir parenteses: exemplos

int()
float()
bool()
str()
...

"""


