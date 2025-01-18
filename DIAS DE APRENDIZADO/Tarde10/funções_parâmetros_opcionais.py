"""
Além disso há como organizar o parâmetro de uma função de 
modo que alguns argumentos devam ser passados por posição e
outros por keyword, ou também híbrido (você decide)

"""

# Parâmetro apenas por posição
def carro_1(marca, modelo, ano, placa):
    print(f"Carro salvo com sucesso!\nmarca: {marca}, modelo: {modelo}, ano: {ano}, placa: {placa}\n")
    
# Parâmetro por posição e por Keyword: A partir do '*' é keyword
def carro_2(marca, modelo, *, ano, placa):
    print(f"Carro salvo com sucesso!\nmarca: {marca}, modelo: {modelo}, ano: {ano}, placa: {placa}\n")
    
# Parâmetro apenas por keyword
def carro_3(*,marca, modelo, ano, placa):
    print(f"Carro salvo com sucesso!\nmarca: {marca}, modelo: {modelo}, ano: {ano}, placa: {placa}\n")
    
# Parâmetro Híbrido: A partir do '/' é opcional, pode ser por keyword ou por posição
def carro_4(marca, /, modelo, ano, placa):
    print(f"Carro salvo com sucesso!\nmarca: {marca}, modelo: {modelo}, ano: {ano}, placa: {placa}\n")
    

carro_1('Ferrari', 'fusca', '1980', '543G-450') # apenas por posição

carro_2('Fiat','Opalla', ano='2007', placa='324L-157') # por posição e por keyword

carro_3(placa='678J-459', ano='2017', modelo='SUV', marca='Volkswagen') # apenas por keyword

carro_4('Chevrolet', placa='356U-443', modelo= 'Esportivo', ano = '2001',) # híbrido 