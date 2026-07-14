class Telefono:
    def __init__(self):
        self.__telefonoFijo = 0
        self.__telefonoMovil = 0
        self.__telefonoTrabajo = 0
    def getTelefonoFijo(self):
        return self.__telefonoFijo
    def getTelefonoMovil(self):
        return self.__telefonoMovil
    def getTelefonoTrabajo(self):
        return self.__telefonoTrabajo
    def setTelefonoFijo(self, numero):
        self.__telefonoFijo = numero
    def setTelefonoMovil(self, numero):
        self.__telefonoMovil = numero
    def setTelefonoTrabajo(self, numero):
        self.__telefonoTrabajo = numero