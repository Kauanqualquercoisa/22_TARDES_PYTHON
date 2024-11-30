""" 
Conjuntos em Pyhon não permitem acessar seus elementos indidualmento 
ao explicitar seus índices como em Tuplas e Listas. Então para fazer
esse acesso por índices devemos converter o conjunto para uma lista.

"""

conjunto = {1,2,3,4,5 } 

conjunto[0] # isso causa um erro

conjunto = list(conjunto)

print(conjunto[0]) # 1