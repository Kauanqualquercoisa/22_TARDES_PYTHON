""" 
Em Python é possível utilizar strings múltiplas ou triplas
elas servem para montar uma string só de forma mais organizada
de sua preferência, caso queira montar um menu por exemplo
"""

nome = 'Kauã'

mensagem = f"""Olá meu nome é {nome}
                   Tenho interesse em programação
              Acredito que é um conhecimento muito útil para minha formação
                   É isso."""
                   
print(mensagem)

# Ao fazer a impressão observamos que os espaços foram preservados e a impressão
#fica exatamente do jeito que formatamos no código, sem a necessidade de usar o \n.