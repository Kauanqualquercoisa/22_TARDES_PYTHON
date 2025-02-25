""" 
Implementação desse diagrama em herança simples em python

              VEICULO
                 ↑
                 |
     —— —— —— ——  —— —— —— ——
     |           |           | 
 Motocicleta    Carro    Caminhão 

"""

class veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = numero_rodas

    def ligar_motor(self):
        
        print("Ligando motor...")
        print(self.cor)
            
class carro(veiculo):
    
    def __init__(self, cor, placa, numero_rodas, janela):
        self.janela = janela
        self.cor = cor
        self.placa = placa
        self.rodas = numero_rodas
                
    def estado_janela(self):
        print(f"A janela {"está" if self.janela else "não está"} fechada")

class motocicleta(veiculo):
    pass

class caminhão(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado): 
        
        super().__init__(cor, placa, numero_rodas) # reutiliza todo os atributos da classe veiculo, sem a necessidade de replica código
        self.carregado = carregado
       
        
    def esta_carregado(self):
        print(f"O caminhão {"Está" if self.carregado else "Não está"} carregado")


moto = motocicleta('Verde', 'gtx-1050', 2)

moto.ligar_motor()

caminhao = caminhão('Vermelho', 'ESV-1930', 8, False)  

caminhao.ligar_motor()

caminhao.esta_carregado()

carro = carro('Cinza', 'MRV-8900', 4, True) # 

carro.ligar_motor()

carro.estado_janela()


""" 
O uso da função super(), basicamente é para evitar de replicar toda a criação dos
atributos da classe pai na classe filho, evitando um retrabalho.

ou seja: 

def __init__(self, cor, placa, numero_rodas, janela):
        self.janela = janela
        self.cor = cor
        self.placa = placa
        self.rodas = numero_rodas
        
é o equivalente a: 

def __init__(self, cor, placa, numero_rodas, janela):
    self.janela = janela
    super().__init__(cor, placa, numero_rodas)


"""