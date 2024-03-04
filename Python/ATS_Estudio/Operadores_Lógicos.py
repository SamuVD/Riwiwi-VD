#Operadores Lógicos 
# a = 10 
# b = 12
# c = 13
# d = 10

# Operacion = ((a > b) or (a < c)) and ((a == c) or (a >= b))
# print(Operacion)

a = 10 
b = 15 
c = 20 

# operacion1 = ((a < b) and (b < c))
# print(operacion1) 

operacion2 = ((a > b) or (b < c))
print(operacion2)

operacion3 = not ((a > b) or (b < c))
print(operacion3)