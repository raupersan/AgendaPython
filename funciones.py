from contacto import Contacto
from agenda import Agenda
def obtenerOpcion(texto):
    leido = False
    while not leido:
        try:
            numero=input(int(texto))
        except ValueError :
            print("ERROR: Tienes que introducir un número")
        else:
            leido = True
    return numero
def mostrarMenu():
    print("##### MENU #####")
    print("1. Mostrar contactos")
    print("2. Buscar contactos")
    print("3. Crear nuevo contacto")
    print("4. Borrar contacto")
    print("5. Guardar contacto")
    print("6. Salir")
def buscarContacto(agenda):
    print("Elige una de las opciones")
    print("1. Buscar por nombre")
    print("2. Buscar por teléfono")
    print("3. Salir")
    fin = False
    while not fin:
        opcion = obtenerOpcion("Opcion:")
        if opcion == 1:
            encontrado = agenda.buscarContactoPorNombre(input(("Introduce el nombre del contacto a buscar")))
            if len(encontrado) > 0: 
                print("##### Contactos encontrados #####")
                for i in encontrado:
                    i.mostrarContacto()
                    print("###############################")
            else:
                print("No se ha encontrado el contacto")
            fin = True
        elif opcion == 2:
            encontrado = agenda.buscarContactoPorTelefono(input(("Introduce el número del contacto a buscar")))
            if len(encontrado) > 0: 
                print("##### Contactos encontrados #####")
                for i in encontrado:
                    i.mostrarContacto()
                    print("###############################")
            else:
                print("No se ha encontrado el contacto")
            fin = True
        elif opcion == 3:
            fin = True
    def procesoCrearContacto(agenda):
        contacto = Contacto()
        contacto.setNombre(input(("Introduce el nombre del contacto: ")))
        contacto.setApellidos(input(("Introduce los apellidos del contacto: ")))
        contacto.setFechaNacimiento(input(("Introduce la fecha de nacimiento del contacto: ")))
        contacto.setEmail(input(("Introduce el correo del contacto: ")))
        contacto.setCalle(input(("Introduce la dirección del contacto: ")))
        contacto.setPiso(input(("Introduce el piso del contacto: ")))
        contacto.setCiudad(input(("Introduce la ciudad del contacto: ")))
        contacto.setCodigoPostal(input(("Introduce el código postal contacto: ")))
        contacto.setTelefonoMovil(input(("Introduce el teléfono móvil del contacto: ")))
        contacto.setTelefonoFijo(input(("Introduce el teléfono fijo del contacto: ")))
        contacto.setTelefonoTrabajo(input(("Introduce el teléfono de trabajo del contacto: ")))
        agenda.crearNuevoContacto(contacto)