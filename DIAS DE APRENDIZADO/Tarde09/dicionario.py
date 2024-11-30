"""" 
Um dicionário é uma estrutura de dados em Python que armazena pares de chave e valor
usado para organizar e acessar dados de forma eficiente, permitindo associar valores 
a uma identificação única (a chave).

Os dicionários são mutáveis, porém suas chaves devem ser estruturas imutáveis como
int,strings ou tuplas, além disso suas chaves precisam ser únicas, não podendo ter 
dauas chaves com o mesmo nome(valor).

"""
# Criação do Dicionário Vazio

dicionário = {}

# Declaração padrão do Dicionário

dicionário = {
    
    'Nome':"Kauã",   # Sendo 'nome' e 'idade' as chaves e 'Kauã' e 19 seus respectivos valores
    'Idade': 19    
}

# Declaração usando o construtor dict()

dicionário = dict(Nome='Kauã',Idade=19) 


