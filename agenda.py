from variables import ruta
from contacto import Contacto
from persona import Persona
class Agenda:
    def __init__(self, path):
        self.__listaContactos = []
        self.__Path = path
    def cargarContactos(self):
        try:
            leerFichero = open(ruta, "r")
        except:
            print("ERROR: Ese fichero no existe")
        else:
            contactos = leerFichero.readlines()
            leerFichero.close()
            if(len(contactos)>0):
                for contacto in contactos:
                    datos = contactos.spli("#")
                    if(len(datos)==11):
                        nuevoContacto = Contacto()
                        nuevoContacto.setNombre(datos[0])
                        nuevoContacto.setApellidos(datos[1])
                        nuevoContacto.setFechaNacimiento(datos[2])
                        nuevoContacto.setEmail(datos[3])
                        nuevoContacto.setCalle(datos[4])
                        nuevoContacto.setPiso(datos[5])
                        nuevoContacto.setCiudad(datos[6])
                        nuevoContacto.setCodigoPostal(datos[7])
                        nuevoContacto.setTelefonoMovil(datos[8])
                        nuevoContacto.setTelefonoFijo(datos[9])
                        nuevoContacto.setTelefonoTrabajo(datos[10])
                        self.__listaContactos = self.__listaContactos + [nuevoContacto]
                print("Se han cargado ", len(self.__listaContactos), " contactos")
    def crearNuevoContacto(self, nuevoContacto):
        self.__listaContactos = self.__listaContactos + [nuevoContacto]
    def guardarContactos(self):
        try:
            fichero = open(self.__Path, "w")
        except:
            print("ERROR: No se puede guardar el fichero")
        else:
            for contacto in self.__listaContactos:
                texto = contacto.getNombre() + "#"
                texto += contacto.getApellido() + "#"
                texto += contacto.getFechaNacimiento() + "#"
                texto += contacto.getEmail() + "#"                
                texto += contacto.getCalle() + "#"
                texto += contacto.getPiso() + "#"
                texto += contacto.getCiudad() + "#"
                texto += contacto.getCodigoPostal() + "#"
                texto += contacto.getTelefonoMovil() + "#"
                texto += contacto.getTelefonoFijo() + "#"
                texto += contacto.getTelefonoTrabajo() + "\n"
                fichero.write(texto)
            fichero.close()
    def mostrarAgenda(self):
        print("###### Agenda ######")
        print("Numero de contactos: ", len(self.__listaContactos))
        for contacto in self.__listaContactos:
            contacto.MostrarContacto()
        print("####################")
    def buscarContactoPorNombre(self, nombre):
        encontrados =[]
        for contacto in self.__listaContactos:
            if contacto.GetNombre() == nombre:
                encontrados+= [contacto]
        return encontrados
    def buscarContactoPorTelefono(self, numero):
        encontrados = []
        for contacto in self.__listaContactos:
            if (contacto.GetTelefonoMovil() == numero | contacto.GetTelefonoFijo() == numero |contacto.GetTelefonoTrabajo() == numero ):
                encontrados += [contacto]
        return encontrados