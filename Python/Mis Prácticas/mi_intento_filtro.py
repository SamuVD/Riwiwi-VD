# # Escribe un programa en Python para gestionar el inventario de una
# # tienda. El programa debe permitir al usuario realizar las siguientes
# # acciones:
# # ● Agregar un nuevo producto al inventario.
# # ● Actualizar la cantidad de un producto existente en el inventario.
# # ● Eliminar un producto del inventario.
# # ● Listar todos los productos en el inventario.
# # ● Verificar si un producto específico está en el inventario.
# # Cada producto en el inventario debe tener los siguientes detalles:
# # ● Nombre del producto
# # ● Precio unitario del producto
# # ● Cantidad disponible en el inventario

Inventario = {}
ejecucion = True

def GestionInventario():
    while (ejecucion):
        OpcionMenu = int(input(f'\n Este es su menú de opciones, por favor seleccione la opción que desea ejecutar: \n \n 1. Agregaré un nuevo producto al inventario. \n 2. Quiero actualizar el precio y la cantidad de productos. \n 3. Deseo eliminar un producto del inventario. \n 4. Quiero ver el inventario de mis productos. \n 5. Necesito verificar si x producto se encuentra en el inventario. \n 6. Cerrar programa. \n'))
        if (OpcionMenu == 1):
            NombreDelProducto = input('Escriba el nombre del producto que desea agregar al inventario: \n').capitalize()
            PrecioDelProducto = float(input('Dame el precio que le pondrás al producto: \n'))
            CantidadDelProducto = int(input(f'Digita la cantidad de producto: \n'))
            Caracteristicas = {'Precio del producto': PrecioDelProducto, 'Cantidad del producto': CantidadDelProducto, }
            Inventario [NombreDelProducto] = Caracteristicas 
            print('-------PRODUCTO AGREGADO AL INVENTARIO-------')
        elif (OpcionMenu == 2):
            NombreDelProducto = input('Escriba de nuevo el nombre del producto ya agredado: ').capitalize()
            PrecioDelProducto = float(input('Dame el nuevo precio que vas actualizar: '))
            CantidadDelProducto = int(input('Ingresa la nueva cantidad que vas a ingresar del producto: '))
            if NombreDelProducto in Inventario:
                Inventario [NombreDelProducto] ['Cantidad del producto'] += CantidadDelProducto
                Inventario [NombreDelProducto] ['Precio del producto'] = PrecioDelProducto
                print(Inventario)
        elif (OpcionMenu == 3):
            EliminarProducto = input('Escriba el nombre del producto que desea eliminar: ').capitalize()
            if EliminarProducto in Inventario:
                del Inventario [EliminarProducto]
                print(Inventario)
        elif (OpcionMenu == 4):
            for NombreDelProducto in Inventario:
                print(f'Nombre del producto: {NombreDelProducto} ')
                print('Precio del producto:', Inventario [NombreDelProducto] ['Precio del producto'])
                print('Cantidad del producto:', Inventario [NombreDelProducto] ['Cantidad del producto'])
                print('-------------------------')
        elif (OpcionMenu == 5):
            NombreDelProducto = input('Escribe el nombre del producto que buscas: ').capitalize()
            if NombreDelProducto in Inventario:
             print(f'\n El producto se encuentra en el inventario.')
            else:
                print('Este producto no existe en el inventario. ')
        elif (OpcionMenu == 6):
            break

GestionInventario()

# Caracteristicas = {'Precio del producto': PrecioDelProducto, 'Cantidad del producto': CantidadDelProducto, }
#             Inventario [NombreDelProducto] = Caracteristicas
#             print(f'Este es el contenido que existe en el inventario: {Inventario} \n ')
