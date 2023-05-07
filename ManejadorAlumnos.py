import numpy as np
import csv
from classAlumnos import Alumno

class Manejador_Alumnos:
    __Alumnos = np.empty(0, dtype=Alumno)

    def __init__(self):
        self.__Alumnos = np.empty(0, dtype=Alumno)
    
    def cargarDatos(self, archivo):
        cabecera = True
        with open(archivo) as f:
            reader = csv.reader(f, delimiter=";")
            for fila in reader:
                if cabecera:
                    cabecera = False
                else:
                    dni = int(fila[0])
                    apellido = fila[1]
                    nombre = fila[2]
                    carrera = fila[3]
                    año = int(fila[4])
                    alumno = Alumno(dni, apellido, nombre, carrera, año)
                    self.__Alumnos = np.append(self.__Alumnos, alumno)

    def alumnoPromocional(self, lista):
        print("DNI\t\tApellido y Nombre\tFecha\t\tNota\tAño que cursa")
        for alumnoP in lista:
            for alumno in self.__Alumnos:
                if alumnoP.getDni() == alumno.getDni():
                    dni=alumno.getDni()
                    apellido=alumno.getApellido()
                    nombre=alumno.getNombre()
                    fecha=alumnoP.getFecha()
                    nota=alumnoP.getNota()
                    año=alumno.getAño()
                    print(f"{dni}\t{apellido} {nombre}\t\t{fecha}\t{nota}\t{año}")

    def listaAlumnosOrdenado(self):
        lista=np.sort(self.__Alumnos)
        print("Lista ordenada por año que cursan y alfabéticamente por apellido y nombre:")
        for alumno in lista:
            print(f"Año: {alumno.getAño()}, Apellido y Nombre: {alumno.getApellido()} {alumno.getNombre()}")

