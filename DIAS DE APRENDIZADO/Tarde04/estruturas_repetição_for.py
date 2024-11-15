"""  
Em Python, as estruturas de repetição são
formadas basicamente por for e while, mas 
tem algumas diferenças em relação a outras 
linguagens

"""

vogais = "aeiouAEIOU"
numero_vogais = 0
palavra = input("Escreve uma palavra: ")

 
for x in palavra: # x recebe em cada iteração o caracter da string digita pelo usuário em palavra
    if x in vogais: # faz uma condição que caso o caracter da vez seja uma vogal imprime essa vogal e soma 1 a contagem
        print(x, end="") # o end="" serve para não pular linha durante a impressão só no final da string
    
        numero_vogais +=1

print(f"\nn° de vogais: {numero_vogais}")

""" 
FUNÇÃO RANGE: uma função built-in do Python usada 
para produzir uma sequência a partir de uma 
definição de começo e fim. Essa função fica mais 
interessante quando juntamos ela com o loop for.

"""

#exemplo de Range simples:

print(list(range(0,4))) # imprime [0,1,2,3]

# o range sozinho gera essa sequência e o list converte para um lista e exibe com o print

# agora range com for..

for numero in range(0,10):
    print(numero, end="") # vai imprimir 0123456789, 10 numeros começando do 0
    
# tabuada do 5 por exemplo
print("")

for numero in range(5,51,5):
    print(numero, end=" ")

