""" 
Em Python há três maneira de fazer a interpolação de variáveis
que é insirir numa string o valor de variáveis de forma concatenada,
são eles: Old Style, Metodo Format e 

"""

# Old Style: Forma não usual de interpolar variaveis em uma string

nome = 'Kauã'
idade = 19
profissão = "engenheiro"
salário = 700.5123

print('Olá me chamo %s tenho %d anos de idade sou %s e recebo mensalmente %.2f R$.' 
                                                                %(nome, idade, profissão, salário))

# Metodo Format: Parecido com o Old Style

print('Olá me chama {} tenho {} anos de idade sou {} e recebo {} R$ por mês.' 
                                                          .format(nome, idade, profissão, salário))

# podemos mudar a sequência da aparição das variáveis da seguinte forma:
# destacando o índice da variável na passagem de argumentos do método .format
print('Olá me chama {2} tenho {1} anos de idade sou {3} e recebo {0} R$ por mês.' 
                                                          .format(nome, idade, profissão, salário))

# F-string: Formato mais usual para interpolação de variáveis em uma string

print(f"Olá me chamo {nome} tenho {idade} anos de idade, sou {profissão} e recebe mensalmente {salário} R$")

#forma de limitar o numero de casas decimais no f - string:

print(f"salário: {salário:.1f}")