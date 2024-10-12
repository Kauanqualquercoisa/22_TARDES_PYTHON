""" 
While é usado quando não sabemos o numero exato de 
repetições que irão acontecer.

"""
# exemplo

opção = -1 # incialmente é -1 permitindo a primeira entrada no while

while opção != 0:
    opção = int(input(" [1] Sacar \n [2] Extrato \n [0] Sair \n : ")) 
# apresenta as opções que vão mudar o valor da variavel "opção" e dita
# se o comando while vai continuar sendo executado a partir da primeira vez
    if opção == 1:
        print("sacando...")
    elif opção == 2:
        print("baixando extrato...")
    else:
        print("saindo...")

        
