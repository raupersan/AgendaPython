from variables import ruta
from contacto import Contacto
from persona import Persona
class Agenda:
    def __init__(self):
        self.listaContactos = []
    def cargarContactos(self):
        leerFichero = open(ruta, "r")
        self.listaContactos = leerFichero.read()
        print(self.listaContactos)
        leerFichero.close()
    def crearNuevoContacto(self):
        contacto = contacto()
        print("Creando nuevo contacto")
        nombre = input(str("Introduce el nombre del contacto"))
        contacto.setNombre
        
        self.listaContactos.append(contacto)
        nuevoContacto = open(ruta,"a")
        nuevoContacto.write(contacto)

    def guardarContactos(self, contacto):
        self.guardarContacto = open(ruta, "a")
        #nuevoContacto = self.cargarContactos
        self.listaContactos.append(contacto)

pruebaAgenda = Agenda()
pruebaAgenda.listaContactos += "a"
pruebaAgenda.listaContactos += "b"
contactos = pruebaAgenda.listaContactos
for contacto in contactos:
    print(contacto)