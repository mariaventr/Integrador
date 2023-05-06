from classMenu import Menu
from ManejadorAlumnos import Manejador_Alumnos
from ManejadorMaterias import Manejador_Materia

def test():
    menu = Menu()
    materias = Manejador_Materia()
    materias.cargarDatos("materiasAprobadas.csv")
    alumnos = Manejador_Alumnos()
    alumnos.cargarDatos("alumnos.csv")
    menu.ejecutar(materias, alumnos)

if __name__== "__main__":
    test()