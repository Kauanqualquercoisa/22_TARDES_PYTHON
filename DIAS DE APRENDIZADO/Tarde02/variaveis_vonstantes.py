"""
 
    Em Python é possivel criar varias variaveis na mesma linha
    basta separá-las por vírgula e atribuir seus respectivos
    valores utilizando parenteses e vírgula também    
    
"""

age = 19
name = "Kauã"
print(f"O meu nome é {name} e eu tenho {age} anos")

age, name = (19, "Kaua")
print(f"Meu nome é {name} e eu tenho {age} anos")

""" 
Em Python não existe um comando que faz uma variavel tornar-se
constante como 'final' em JAVA ou 'const' em C.
Uma convenção usada para dizer que uma variavel 
será constante basta nomear a  variavel com valores em letra MAIÚSCULA.

"""

AGE = 20 # EU ESTOU DIZENDO PARA QUEM LER O CÓDIGO QUE AGE É CONSTANTE.
print(AGE)

BRAZILIAN_STATES = ["SP","ES","RJ","BA"]

print(BRAZILIAN_STATES)


