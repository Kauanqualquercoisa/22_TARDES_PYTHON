""" 
Em Python, manipular strings é bem mais fácil do que em outras linguagens,
pois já existem métodos que facilitam o trabalho do programador, vejamos alguns
deles, que são mais simples.
 
"""

# MAIÚSCULA, minúscula e Título - Métodos

curso = "PyThOn" # uma string com letras Maiúsculas e Minúsculas misturadas

curso = curso.upper() # método upper() deixa toda a string em MAIÚSCULO

print(f"Método Upper(): {curso}")

curso = curso.lower() # método lower() deixa toda a string em MINÚSCULO

print(f"Método lower(): {curso}")

curso = curso.title() # método title() deixa apenas o primeiro caracter em MAIÚSCULO e o resto minúsculo

print(f"Método title(): {curso}")


  