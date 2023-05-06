class Materia:
    __dni=0
    __nombre=""
    __fecha=""
    __nota=0
    __aprobacion=""
    def __init__(self, dni,nombre,fecha,nota,aprobacion):
        self.__dni=dni
        self.__nombre=nombre
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion

    def getDni(self):
        return self.__dni

    def getNota(self):
        return self.__nota
    
    def getMateria(self):
        return self.__nombre
    
    def getFecha(self):
        return self.__fecha
    