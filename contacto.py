from direccion import Direccion
from persona import Persona
from telefono import Telefono

class Contacto(Direccion, Persona, Telefono):
    def __init__(self):
        self.__email = ""
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email
    def mostrarContacto(self):
        print("\tNomrbre del contacto: ", self.getNombre())
        print("\tApellidos del contacto: ", self.getApellidos())
        print("\tFecha de nacimiento del contacto: ", self.getFechaNacimiento())
        print("\tCorreo del contacto: ", self.getEmail())
        print("\tCalle del contacto: ", self.getCalle())
        print("\tPiso del contacto: ", self.getPiso())
        print("\tCiudad del contacto: ", self.getCiudad())
        print("\tCódigo postal del contacto: ", self.getCodigoPostal())
        print("\tTeléfono fijo del contacto: ", self.getTelefonoFijo())
        print("\tTelefono móvil del contacto: ", self.getTelefonoMovil())
        print("\tTelefono de trabajo del contacto: ", self.getTelefonoTrabajo())
"""
contactoNuevo = Contacto()
contactoNuevo.setNombre(input(str("Introduce el nombre del contacto "))) 
contactoNuevo.setApellidos(input(str("Introduce el apellido del contacto ")))
contactoNuevo.setFechaNacimiento("c") 
contactoNuevo.setEmail("d") 
contactoNuevo.setCalle("e") 
contactoNuevo.setPiso("f") 
contactoNuevo.setCiudad("g") 
contactoNuevo.setCodigoPostal(1) 
contactoNuevo.setTelefonoFijo(2) 
contactoNuevo.setTelefonoMovil(3) 
contactoNuevo.setTelefonoTrabajo(4) 
print(len(vars(contactoNuevo)))
contactoNuevo.mostrarContacto()
"""