""" 
O método construtor sempre é executado quando uma nova instância da classe é criada. 
Nesse método inicializamos o estado do nosso objeto. 
Para declarar o método construtor da classe, criamos um método com o nome __init__.

"""

#exemplo de uso de construtor ou inicializador

class Carro:
    def __init__(self, modelo, ano):  # Construtor
        
        self.modelo = modelo  # Atributo salvo na memória
        self.ano = ano  # Atributo salvo na memória
        

meu_carro = Carro("Fusca", 1975)  # O construtor é chamado automaticamente
print(meu_carro.modelo)  # Saída: Fusca
        
# 🔎 Internamente, o Python faz isso:

# Chama __new__() → Aloca espaço na Heap
# Chama __init__() → Define self.modelo = "Fusca" e self.ano = 1975
# Retorna o objeto criado e associa à variável meu_carro
    
""" 
O método __del__ é um destrutor, chamado quando um objeto é removido da memória. 
Ele libera recursos antes do objeto ser destruído pelo Garbage Collector (GC).  

"""       
# Exemplo de destrutor

class Exemplo:
    def __init__(self):
        print("Objeto criado!")

    def __del__(self):
        print("Objeto destruído!")

obj = Exemplo()
del obj  # Chama __del__()

# 🔎 Internamente, o Python faz isso:

# Aloca o objeto na Heap
# Associa a variável obj ao objeto
# Quando del obj é chamado, reduz a contagem de referências do objeto
# Se não houver mais referências, o Garbage Collector remove o objeto da memória e chama __del__()

# OBS: o Garbage Collector é remove o objeto da memória com ou seu o uso do "del obj", ou seja, o método
# del sempre é chamado