class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = {
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4
        }

    def opcion1(self, materia):
        print("Informar Promedio.")
        dni=int(input("Ingresar DNI: "))
        materia.promedioConAplazos(dni)
        materia.promedioSinAplazos(dni)
        
    
    def opcion2(self, materia, alumno):
        print("Estudiantes con Promocionalidad.")
        nombre_materia=input("Ingresar el nombre de la Materia: ")
        listaEstProm=materia.estudiantesProm(nombre_materia)
        if len(listaEstProm)==0:
            print(f"No hay ningun almunno que haya promocionado la Matteria: {nombre_materia}")
        else: alumno.alumnoPromocional(listaEstProm)

    def opcion3(self, alumno):
        print("Listado de alumnos.")
        alumno.listaAlumnosOrdenado()
    
    def opcion4(self):
        print("Usted esta saliendo del Programa")
        
        
    def ejecutar(self, manejadorM, manejadorA):
            while True:
                print("Bienvenido al menú de opciones")
                print("1. Informar Promedio.")
                print("2. Estudiantes con Promocionalidad.")
                print("3. Listado de alumnos.")
                print("4. Salir")
                op = int(input("Ingrese una Opcion: "))

                # Utilizamos el switcher para llamar a la función correspondiente a la opción seleccionada
                func = self.__switcher.get(op, lambda: print("Opción no válida"))
                if op==1:
                    func(manejadorM)
                elif op==2:
                    func(manejadorM, manejadorA)
                elif op==3:
                    func(manejadorA)
                else: 
                    func()
                if 4==op:
                    break

