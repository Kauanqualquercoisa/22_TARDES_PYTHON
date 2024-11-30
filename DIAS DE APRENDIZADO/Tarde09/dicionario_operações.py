""" 
Os dicionários são mutáveis, portanto é possivel realizar
operações de adição, remoção e atualização de suas chaves 
e valores.

"""
dicionário = {
    'nome':'Kauã',
    'idade':19
    } # Inicialmente a variável só tem 2 chaves e 2 valores

# Adição 
dicionário['Profissão'] = 'Engenheiro' # Agora a variável passa a ter 3 chaves e 3 valores.

# Atualização
dicionário['idade'] = 20 # Aqui eu atualizei o valor de uma variável que já existia no dicionário

# Acesso às informações em Dicionário

print(dicionário['nome']) # Kauã
print(dicionário['idade']) # 20
 
# Ou seja para acessar as informações no dicionário basta indexar sua chave

""" 
Para remover valores podemos del ou o método pop()

O del remove o par chave:valor e não retorna nada
O método pop() remove o par chave:valor e retorna o par removido

"""
# Remoção com del

del dicionário['Profissão'] # Removeu a chave Profissão e seu respectivo valor "Engenheiro" do dicionário

idade = dicionário.pop('idade') # Removeu a chave idade e seu respectivo valor 20 do dicionário

# a variável idade recebe o valor da chave idade que foi removida

print(idade) # 20

print(dicionário) # só sobrou {"nome":"Kauã"}

