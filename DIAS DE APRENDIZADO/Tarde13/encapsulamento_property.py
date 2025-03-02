""" 
A função property, também chamado de decorador, em Python permite controlar o acesso a atributos de 
uma classe, fornecendo um meio seguro para ler, modificar e até proteger dados sem expô-los diretamente.

Ela age como um getter e setter
"""
# Exemlo sem o property, usando o get e setter:
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    def get_nome(self): # Getter
        return self.__nome
    
    def set_nome(self, novo_nome): # Setter
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            print('Nome inválido')
    
p = Pessoa('Kauã')
print(p.get_nome()) # Kauã

p.set_nome('Kauan')   
print(p.get_nome()) # Kauan

# Exemplo com property

class Pessoa1:
    def __init__(self, nome):
        self.__nome = nome # Atributo privado
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter    # Define um setter
    def setar_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            print('Nome inválido')
    
p1 = Pessoa1('Kauã')

print(p1.nome) # imprimindo a valor no atributo privado __nome

p1.setar_nome = 'Kauan' # Settando o "Kauan" para o atributo privado __nome
print(p1.nome)
    
        