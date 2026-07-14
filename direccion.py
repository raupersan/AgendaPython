class Direccion:
    def __int__(self):
        self.__calle = " "
        self.__piso = 0
        self.__ciudad = " "
        self.__codigoPostal = 0
    def getCalle (self):
        return self.__calle
    def getPiso(self):
        return self.__piso
    def getCiudad(self):
        return self.__ciudad
    def getCodigoPostal(self):
        return self.__codigoPostal
    def setCalle (self, calle):
        self.__calle = calle
        return calle
    def setPiso (self, piso):
        self.__piso = piso
        return piso
    def setCiudad (self, ciudad):
        self.__ciudad = ciudad
        return ciudad
    def setCodigoPostal (self, codigoPostal):
        self.__codigoPostal = codigoPostal
        return codigoPostal

    

    
    

