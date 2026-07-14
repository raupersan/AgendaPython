class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__apellidos = ""
        self.__fechaNacimiento = ""
    def getNombre(self):
        return self.__nombre
    def getApellidos(self):
        return self.__apellidos
    def getFechaNacimiento(self):
        return self.__fechaNacimiento
    def setNombre (self, nombre):
        self.__nombre = nombre
    def setApellidos(self, apellido):
        self.__apellidos = apellido
    def setFechaNacimiento(self, fecha):
        self.__fechaNacimiento = fecha
