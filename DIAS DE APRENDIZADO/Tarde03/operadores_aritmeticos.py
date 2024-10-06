x =10
y = 2

print(x+y) # soma
print(x-y) # sub
print(x*y) # multi
print(x**y) # expo
print(x/y) # divisão que retorna um valor do tipo float
print(x//y) # divisão que retorna um valor do tipo int
print(x%y) # resto da divisão

# Precedências

z = 10 + 5 * 4
print(z)

z = (10+5) * 4 # se colocar parenteses a precedência muda priorizando os "()"
print(z)

z = 10-2+8**2*4/4 # O python vÊ : 10-2 + (8**2) * 4/4 -> 10-2 + 64*1 -> 8 + 64 = 72

print(z)