# def agregar_tarea(lista_tareas):
#     nombre_tarea = input("Ingrese el nombre de la tarea: ")
#     tarea = {"tarea": nombre_tarea, "completada": False}
#     lista_tareas.append(tarea)
#     print("Tarea agregada con éxito.")


# def modificar_tarea(lista_tareas):
#     mostrar_tareas(lista_tareas)
#     indice = int(input("Ingrese el número de la tarea que desea modificar: ")) - 1
#     if 0 <= indice < len(lista_tareas):
#         nombre_nuevo = input("Ingrese el nuevo nombre de la tarea: ")
#         lista_tareas[indice]["tarea"] = nombre_nuevo
#         print("Tarea modificada con éxito.")
#     else:
#         print("Índice de tarea fuera de rango.")


# def eliminar_tarea(lista_tareas):
#     mostrar_tareas(lista_tareas)
#     indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
#     if 0 <= indice < len(lista_tareas):
#         del lista_tareas[indice]
#         print("Tarea eliminada con éxito.")
#     else:
#         print("Índice de tarea fuera de rango.")


# def verificar_tarea(lista_tareas):
#     mostrar_tareas(lista_tareas)
#     indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
#     if 0 <= indice < len(lista_tareas):
#         lista_tareas[indice]["completada"] = True
#         print("Tarea marcada como completada.")
#     else:
#         print("Índice de tarea fuera de rango.")


# def mostrar_tareas(lista_tareas):
#     if not lista_tareas:
#         print("No hay tareas en la lista.")
#     else:
#         print("Lista de tareas:")
#         for i, tarea in enumerate(lista_tareas, 0):
#             estado = "Completada" if tarea["completada"] else "Pendiente"
#             print(f"{i}. {tarea['tarea']} - Estado: {estado}")


# def main():
#     lista_tareas = []
#     while True:
#         print("\nMenú de opciones:")
#         print("1. Agregar tarea")
#         print("2. Modificar tarea")
#         print("3. Eliminar tarea")
#         print("4. Verificar tarea")
#         print("5. Mostrar tareas")
#         print("6. Salir")

#         opcion = input("Ingrese el número de la opción que desea realizar: ")

#         if opcion == "1":
#             agregar_tarea(lista_tareas)
#         elif opcion == "2":
#             modificar_tarea(lista_tareas)
#         elif opcion == "3":
#             eliminar_tarea(lista_tareas)
#         elif opcion == "4":
#             verificar_tarea(lista_tareas)
#         elif opcion == "5":
#             mostrar_tareas(lista_tareas)
#         elif opcion == "6":
#             print("¡Hasta luego!")
#             break
#         else:
#             print("Opción inválida. Por favor, ingrese un número válido.")


# main()


# convocatory = []

# def DataBase(options):
#     while (options):
#         Listings = int(input('\n Acá podrá actualizar la base de datos para la multinacional. \n \n 1. Agregar un candidato. \n 2. Eliminar un candidato. \n 3. Modificar algún candidato. \n 4. Listado de candidatos. \n \n INGRESE EL # DE LA FUNCIÓN QUE VA REALIZAR: '))
#         if (Listings == 1):
#             AddCandidate = {}
#             AddCandidate ['Name'] = input('\n Ingrese el nombre del candidato: ').capitalize()
#             AddCandidate ['WorkExperency'] = int(input(f'\n ¿Cuántos años de experiencia laboral tiene? : '))
#             if AddCandidate ['WorkExperency'] in range (5, 20):
#                     print('\n----El candidato aplica para la multinacional.----')
#                     AddCandidate ['Elegible'] = True
#             elif AddCandidate ['WorkExperency'] in range (0,4) or AddCandidate ['WorkExperency'] > 20:
#                     print('\n----El candidato no aplica para la multinacional.----')
#                     AddCandidate ['Elegible'] = False
#             AddCandidate ['DeveloperLanguages'] = int(input('\n¿Cuántos idiomas de desarrollo domina? : '))
#             if AddCandidate ['DeveloperLanguages'] in range (10,15):
#                     print('\n----EL candidato aplica para el trabajo.----')
#                     AddCandidate ['Elegible'] = True
#             elif AddCandidate ['DeveloperLanguages'] < 10:
#                     print('\n----El candidato no aplica para el trabajo.----')
#                     AddCandidate ['Elegible'] = False    
#             AddCandidate ['Languages'] = input('\n¿Maneja el idioma inglés? : ')
#             if AddCandidate ['Languages'] == 'Si':
#                     print('\n----Es apto.----')
#                     AddCandidate ['Elegible'] = True
#             elif AddCandidate ['Languages'] != 'Si':
#                     print('\n----No es apto.----')  
#                     AddCandidate ['Elegible'] = False
#             convocatory.append(AddCandidate)
 
# DataBase(options=True)
