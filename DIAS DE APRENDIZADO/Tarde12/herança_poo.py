""" 
Herança em Python é a capacidade de uma classe "filha" derivar ou herdar características
e comportamentos (atributos e métodos) da classe "pai"

O conceito de heraça é de natureza transitiva, o que significa que, se a classe B herdar 
a classe A, todas as subclasses de B herdarão automaticamente da classe A. E assim sucessivamente
"""
# Exemplo básico da sintaxe da herança:

class A():
    pass

class B(A): # A classe B foi criada sendo uma classe "filha" da classe A 
    pass

class C(B): # Aqui a classe C é "filha" da classe B e "neta" da classe A e assim sucessivamente
    pass


""" 

Herança múltipla, quando uma classe filha herda de várias classes pai

"""
# Exemplo de herança múltipla

class D(A, B): # Aqui a classe D é "filha" tanto da classe A quanto da classe B
    pass