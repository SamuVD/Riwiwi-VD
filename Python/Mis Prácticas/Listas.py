""" se hace una convocatoria para elegir candidatos para una multinacional. 
La información que se debe tener de los candidatos es: 
nombre, experiencia laboral en años, lenguajes de programación que domina, 
idiomas...Las funciones que debe tener el código son: Agregar candidatos,
Eliminar candidatos, Modificar candidatos, Mostrar candidatos.  QUE COMIENCE EL JUEGO!! """
convocatory = []
addCandidate = {}
def DataBase():
    while (True):
        Listings = int(input('\n Acá podrá actualizar la base de datos para la multinacional. \n \n 1. Agregar un candidato. \n 2. Eliminar un candidato. \n 3. Modificar algún candidato. \n 4. Listado de candidatos. \n 5. Salir del listado de la convocatoria. \n \n INGRESE EL # DE LA FUNCIÓN QUE VA REALIZAR: '))
        if (Listings == 1):
            Name = input('\n Ingrese el nombre del candidato: ').capitalize()
            WorkExperency = int(input(f'\n ¿Cuántos años de experiencia laboral tiene? : '))
            if WorkExperency in range (5, 20):
                    print('\n----El candidato aplica para la multinacional.----')
            elif WorkExperency in range (0,4) or WorkExperency > 20:
                    print('\n----El candidato no aplica para la multinacional.----')
            DeveloperLanguages = int(input('\n¿Cuántos idiomas de desarrollo domina? : '))
            if DeveloperLanguages in range (10,15):
                    print('\n----EL candidato aplica para el trabajo.----')
            elif DeveloperLanguages < 10:
                    print('\n----El candidato no aplica para el trabajo.----')    
            Languages = input('\n¿Maneja el idioma inglés? : ')
            if Languages == 'Si':
                    print('\n----Es apto.----')
            elif Languages != 'Si':
                    print('\n----No es apto.----')
            addCandidate [Name] = WorkExperency   
            print('\n----"EL CANDIDATO FUE AGREGRADO CON ÉXITO"----')
            convocatory.append(addCandidate)
        if (Listings == 2):
            DeleteCandidate = input('\nPor favor escribe el nombre del candidato que vas a eliminar: ').capitalize()
            if DeleteCandidate in convocatory:
                  convocatory.remove(DeleteCandidate)
                  print('\n"El candidato ha sido eliminado exitosamente" \n')
        if (Listings == 3):
              Name = input('\nDeme el nombre del candidato que desea modificar: ').capitalize()
              WorkExperency = int(input('\nActualice sus años de experiencia: '))
              DeveloperLanguages = int(input('\nActualice el número de idiomas que domina: '))
              if  Name in addCandidate:
                    addCandidate [Name] ['WorkExperency'] = WorkExperency
                    addCandidate [Name] ['DeveloperLanguages'] = DeveloperLanguages
                    print(addCandidate)
        if (Listings == 4):   
              for Name in addCandidate:
                    print(f'\nEl candidato es -- {Name}')
                    print('\nExperiencia Laboral:', addCandidate [Name] ['Experiencia laboral'])
                    print('\nIdiomas dominados:', addCandidate [Name] ['Idiomas dominados'])
                    print('\nIdioma requerido:', addCandidate [Name] ['\nIdioma requerido'])
                    print('____________________________')
        elif (Listings == 5):
              print('\n--ADIÓS--')
DataBase()