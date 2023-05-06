import numpy as np
import csv
from classMaterias import Materia

class Manejador_Materia:
    __Materia=[]
    def __init__(self):
        self.__Materia=[]
    
    def cargarDatos(self, archivo):
        cabecera=True
        with open(archivo) as f:
            reader= csv.reader(f, delimiter=(";"))
            for fila in reader:
                if cabecera:
                    cabecera= not cabecera
                else:
                    dni=int(fila[0])
                    nombre=fila[1]
                    fecha=fila[2]
                    nota=int(fila[3])
                    aprobacion=fila[4]
                    materia=Materia(dni,nombre,fecha,nota,aprobacion)
                    self.__Materia.append(materia)
    
    def promedioConAplazos(self, dni):
        notas_alumno=[]
        for materia in self.__Materia:
            if materia.getDni() == dni:
                notas_alumno.append(materia.getNota())
        cantidad_materias = len(notas_alumno)
        suma_notas = sum(notas_alumno)
        promedio = suma_notas / cantidad_materias
        print(f"El promedio con aplazos es: {promedio:.2f}")

    def promedioSinAplazos(self,dni):
        notas_alumno=[]
        for materia in self.__Materia:
            if materia.getDni() == dni and materia.getNota() > 4:
                notas_alumno.append(materia.getNota())
        cantidad_materias = len(notas_alumno)
        suma_notas = sum(notas_alumno)
        promedio = suma_notas / cantidad_materias
        print(f"El promedio sin aplazos es: {promedio:.2f}")
                
    def estudiantesProm(self, nombre):
        alumnos=[]
        for materia in self.__Materia:
            if materia.getMateria() == nombre and materia.getNota() >= 7:
                alumnos.append(materia)
        return alumnos