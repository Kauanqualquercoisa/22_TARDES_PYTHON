""" 
#INPUT

A função input é usada quando queremos ler dados do 
usuário. Ele sempre retorna um valor de string, portanto
é necessário fazer as conversões de tipo caso seja 
necessário, usando os construtores de conversão

"""

nome = input("Digite seu nome: ") # dentro do "()" do input pode-se digitar um comando ao usuário

print(nome)

idade = (input("Sua idade: "))
 
print(f"idade: {idade}, tipo {type(idade)}")

idade = int(input("Sua idade: ")) # para converter para colocar todo o input dentro do construtor int
print(f"idade: {idade}, tipo {type(idade)}")