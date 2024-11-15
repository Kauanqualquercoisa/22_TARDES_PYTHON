""" 
Em Python, as estruturas de condição são:
if,else e elif. Esse último junta os else e 
o if, usado para adicionar mais condiçõs ao
seu códgio, aumentando sua complexidade.

"""

saldo = 500
produto = 550

# simples if e else:
if saldo > produto:
    print("A compra foi realizada")
else:
    print("Saldo insuficiente.")
    
# adicionando uma variável limite podemos aumentar a complexidade com elif
# com o limite o cliente pode conseguir comprar o produto pelo crédito

limite = 1000

if saldo >= produto:
    print("Compra realizada")
elif limite >= produto:
    print("Compra no crédito aprovada")
else:
    print("Saldo e limite insuficiente")
    
""" 
Em Python também existem operadores ternários,
assim como C e Java. Esses operadores realizam 
essas operações condicionais de uma forma mais
enxuta.

"""    

#exemplo

status = "Sucesso" if saldo>=produto else "Falha"

print(f"{status} ao realizar a compra")



