""" 
Exemplo simples da criação de uma classe em Python

João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. 
Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. 
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

"""

class bicicleta():
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor 
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Plim Plim...\n")
    
    def parar(self):
        print("parando...\n")
    
    def correr(self):
        print("Vrummmmmmmmmm...\n")
        
    def trocar_marcha(self, numero_marcha):
        print("Trocando de marcha...\n")
        
        
        def _trocar_marcha_(numero_marcha):
            if numero_marcha > self.marcha:
                print("A marcha foi trocada\n")
            else:
                print("Não foi possível trocar a marcha\n")
        
        _trocar_marcha_(numero_marcha)
        
    
bicicleta1 = bicicleta('Verde','Caloy','2014','570') # criando uma instância da classe bicicleta

# Aplicando os métodos da classe bicicleta
bicicleta1.correr() 

bicicleta1.buzinar()

bicicleta1.parar()

bicicleta1.trocar_marcha(0) # Não será possível trocar a marchar, pois self.marcha foi definido com valor 1

bicicleta1.trocar_marcha(3) # Agora será possivel, já numero_marcha será maior que self.marcha  

# Imprimindo as características da instancia bicicleta1 que foram passadas como argumentos da classe:
print(bicicleta1.ano, bicicleta1.modelo, bicicleta1.cor,bicicleta1.valor)

# Outra forma de executar o método 
bicicleta.buzinar(bicicleta1) # é igual a usar: bicicleta1.buzinar()


            