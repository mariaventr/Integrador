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
        listaAño= sorted(self.__Alumnos, key=lambda x: x.getAño())
        listaAlfabe= sorted(self.__Alumnos, key=lambda x: x.getApellido())
        print("Lista ordenada por Año")
        print("Apellido y Nombre\tAño que Cursa")
        for alumno in listaAño:
            print(f"{alumno.getApellido()} {alumno.getNombre()}\t\t{alumno.getAño()}")
        print("Lista ordenada por Apellido y Nombre ")
        print("Apellido y Nombre\tAño que Cursa")
        for alumno in listaAlfabe:
            print(f"{alumno.getApellido()} {alumno.getNombre()}\t\t{alumno.getAño()}")

