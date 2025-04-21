"""#__str__

class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):                   #__str__ metodo especial que se pasa a string la informacion del objeto 

        return f"Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad}"

p1=Persona("Juan", "Perez", 25)

print(p1)
"""
"""
class Persona():

    almacen_datos = []

    def __init__(self, *datos):                   #*datos es un parametro que recibe una cantidad indefinida de datos

        for dato in datos:                              #lo que hace es almacenar todos los datos en una lista
            
            self.almacen_datos.append(dato)            #almacenamos los datos en la lista almacen_datos

        self.getDatos(self.almacen_datos)                 #llamamos al metodo getDatos y le pasamos la lista almacen_datos
        


    def getDatos(self, info):                               #metodo que recibe una lista de datos

        for dato in info:                      #imprime cada dato de la lista

            print(dato)


p1 = Persona("Juan", "Perez", 25, "Calle 123", "1234567")
"""

class Persona():

    def __init__ (self, **datos):                          #**datos es un parametro que recibe una cantidad indefinida de datos

        elementos=datos.items()                    #items() metodo que devuelve una lista de tuplas con clave y valor

        for clave, valor in elementos:                          #recorremos la lista de tuplas

            print(f"{clave} : {valor}")                          #imprimimos la clave y el valor

p1 = Persona(nombre="Juan", apellido="Perez", edad=25, direccion="Calle 123", telefono="1234567")               #creamos un objeto de la clase Persona y le pasamos los datos