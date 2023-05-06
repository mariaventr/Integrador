class Alumno:
    __dni=0
    __apellido=""
    __nombre=""
    __carrera=""
    __año=0
    def __init__(self, dni,apellido,nombre,carrera,año):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__carrera=carrera
        self.__año=año

    def getDni(self):
        return self.__dni
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getAño(self):
        return self.__año
    
    def __it__(self, otro):
        return self.__año < otro.__año