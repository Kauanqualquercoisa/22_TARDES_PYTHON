"""
Em Python tudo é considerado objeto, portanto as funções também são, assim como
uma string, uma lista ou uma valor inteiro qualquer, logo podem ser atribuidas a
variáveis sem problema nenhuma, ou então podem ser usadas como argumentos para outras
funções.

"""
#exemplo

def somar(a,b):
    return a+b

def exibir_soma(a,b, função): # Aqui o argumento função é usado dentro do código realmente como uma função
    
    resultado = função(a,b) 
    print(f'O resultado da operação {a} + {b} = {resultado}')
    
exibir_soma(10,5,somar) # somar entra no lugar da função passado como argumento em exibir_soma

# atribuindo a função somar a uma variável

variavel = somar

print(variavel(8,9)) # a saída é 17