""" 
Para retornar valores em funções, usamos a palavra 'return'.
Em python é possivel uma função retornar mais de um valor
basta usar a vírgula para diferenciar os valores que serão 
retornados em uma Tupla.

"""

# OBS: Quando não é explicitado o retorno da função, ela retorna None.

def funcao_sem_retorno():
    print("Sem retorno!")


# Exemplo de função com 1 parâmetro e com apenas 1 retorno:
def somatoria(numeros):
    return sum(numeros)

# Exemplo de função com 1 parâmetro e com dois retornos:
def sucessor_antessor(numero):
    sucessor = numero + 1
    antessor = numero - 1
    
    return sucessor, antessor

# Código principal ↓ :

print(funcao_sem_retorno()) # None

somatoria([2,3,4,5]) # 14 - Foi passado uma lista de inteiros e a função retornou a soma desses inteiros.

sucessor_antessor(10) # (11,9) - Retorna um tupla com o valor do primeiro retorno e o segundo retorno.

"""' 
Podemos fazer com que duas variáveis no código principal recebam cada uma
os valores retornados na Tupla de função que retorna mais de uma variável.
Basta usa a vírgula para isso.

"""
sucessor = 0
antecessor = 0

sucessor, antecessor = sucessor_antessor(20)

print(sucessor) # 21
print(antecessor) # 19