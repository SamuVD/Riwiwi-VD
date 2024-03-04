""" Función para mostrar menu """
def mostrarMenu():
    print("\n¿Qué desea realizar?\n1- Agregar un nuevo producto\n2- Actualizar la cantidad de un producto\n3- Eliminar un producto\n4- Listar productos del inventario\n5- Verificar si un producto está en el inventario\n6- Salir del Programa")
    opcionMenu = int(input("Digite la opción: "))
    return opcionMenu

""" Función para agregar un nuevo producto """
def agregarProducto(listanombre, listaPrecio, listaCantidad):
    nombreProducto = input("\nDigite el nombre del producto: ")
    precioProducto = float(input("Digite el precio unitario del producto: "))
    cantidadProducto = int(input("Digite la cantidad disponible del producto: "))

    listanombre.append(nombreProducto.lower())
    listaPrecio.append(precioProducto)
    listaCantidad.append(cantidadProducto)
    
    print("\n-----Producto agregado con éxito-----")

""" Función para actualizar la cantidad de un producto  """
def actualizarCantidadProducto(listaCantidad,codigoProducto, cantidadActualizada):
    listaCantidad[codigoProducto-1] = cantidadActualizada
    print("\n-----Cantidad actualizada con éxito-----")
    
""" Función para mostrar valores de una lista indicada """
def mostrarListas(lista):
    cont=0
    for i in lista:
        cont+=1
        print(f"\nCódigo #{cont}: {i}")

""" Función para mostrar el valor de todas las listas """
def mostrarTotalListas(listanombre, listaPrecio, listaCantidad):
    for nombre,precio, cantidad in zip(listanombre,listaPrecio,listaCantidad):
        print(f"\nNombre del producto: {nombre}, Precio unitario: ${precio}, Cantidad disponible: {cantidad}") 

""" Función para eliminar un producto """
def eliminarProducto(codigoProducto, listaCantidad, listaNombreProducto, listaPrecioProducto):
    listaCantidad.pop(codigoProducto-1)
    listaNombreProducto.pop(codigoProducto-1)
    listaPrecioProducto.pop(codigoProducto-1)
    print("\n-----Producto eliminado con éxito-----")


""" INICIO DE LA LÓGICA DE NEGOCIO """
""" Gestión de inventario """

""" Definición de variables """
listaNombreProducto = []
listaPrecioProducto = []
listaCantidadProducto = []
continuarPrograma = True
cont=0

print("Bienvenido a la gestión del inventario")

""" Ciclo para iteración del programa """
while continuarPrograma:

    opcionMenu = mostrarMenu()

    """ Gestionar opciones disponibles en el menu """
    match opcionMenu:
        case 1:
            agregarProducto(listaNombreProducto, listaPrecioProducto, listaCantidadProducto)
        case 2:
            mostrarListas(listaNombreProducto)
            numProductoActualizar = int(input("\nDigite Codigo del producto al que va a actualizar: "))
            valorActualizarCant = int(input("Digite la cantidad actualizada del producto: "))
            actualizarCantidadProducto(listaCantidadProducto, numProductoActualizar, valorActualizarCant)
        case 3:
            mostrarListas(listaNombreProducto)
            productoEliminar = int(input("\n¿Qué producto desea eliminar?: "))
            eliminarProducto(productoEliminar,listaCantidadProducto,listaNombreProducto,listaPrecioProducto)
        case 4:
            mostrarTotalListas(listaNombreProducto,listaPrecioProducto, listaCantidadProducto)    
        case 5:
            buscarProducto = input("Digite el producto que desea buscar: ")
            for producto in listaNombreProducto:
                if producto == buscarProducto.lower():
                    print(f"\n-----El producto está en el inventario-----")
                    break
                else:
                    print(f"\n-----El producto no está en el inventario-----")
        case 6:
            continuarPrograma = False
            print("\nSaliendo del programa, ¡Feliz día!\n")
        case _:
            print("\n-----OPCIÓN NO VÁLIDA-----")