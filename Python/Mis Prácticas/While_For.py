# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.

asignaturas = []
contador = 0

while contador < 5 : 
    print("El contador", contador)
    asignar = input("por favor ingrese la asignatura: ")
    asignaturas.append(asignar)
    contador += 1

for cla in asignaturas:
    print(f"Tu asignatura es: {cla}")                                                                                                   
    