""" 
As funções são blocos de códigos identificados por um nome que pode
receber parâmetros de entradas e pode retornar um valor de saída.
São úteis para tornar o código mais legível e 'economico', pois podem ser
chamadas várias vezes ao longo do código.

Em Python as funções são declaradas ao usar a palavra "def"
e seguida inserir o nome da função e seus parâmetros.

"""

# exemplo de função sem parâmetro e sem retorno:
def funcao_imprimir_mensagem():
    
    print('Olá Mundo!')

# exemplo de função com parâmetro e sem retorno:
def funcao_boas_vindas(nome):
    
    print(f"Seja bem-vindo {nome}")
    
# exemplo de função com parâmetro e sem retorno tipo 2:    
def funcao_boas_vindas_2(nome='Unknown'):
    
    print(f"Seja bem vindo: {nome}")

# Código principal ↓ :

# Chamando as funções no código principal

funcao_imprimir_mensagem() 

funcao_boas_vindas('Kauã') # A String Kauã é o parâmetro exigido pela função.

funcao_boas_vindas_2() # Caso você não passe o parâmetro para a função, o 'Unknown' irá ocupar esse espaço.

funcao_boas_vindas_2('Python') # Aqui a função ignora o 'Unknown' e receber o parâmetro que foi passado.
