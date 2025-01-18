""" 
Funções também podem ser chamdas usando argumentos nomeados 
da forma chave=valor

"""

# Exemplo prático:

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro salvo com sucesso!\nmarca: {marca}, modelo: {modelo}, ano: {ano}, placa: {placa}\n")


# Código principal ↓ :

#Primeira forma:
salvar_carro('fiat','SUV','1990','890M-1243')

#Segunda forma: A vantagem é que não é necessário passar os parâmetros na ordem estabelicida na função
salvar_carro(marca='fiat',ano='2010',modelo='opala',placa='494M-3553')

#Terceira forma: passando um dicionário como argumento, onde o próprio interpretador vai relacionar os parâmetros
salvar_carro(**{'marca':'Fiat', 'ano':'2007', 'placa':'454Y-3430', 'modelo':'palio'}) # funciona igual a segunda forma





    
