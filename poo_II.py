"""
class Persona:

    nombre = ""
    apellido = ""
    edad = 0
    genero = "sin definir"

    def hablar(self):

        return f"La persona que se llama {self.nombre} está hablando"
    
    def camina(self):

        return f"La persona que se llama {self.nombre} está caminando"
    
    def getDatos(self):

        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, \
Edad: {self.edad}, Genero: {self.genero}"
    

p1 = Persona()

p1.nombre = "Juan"
p1.apellido = "Perez"

print(p1.getDatos())
"""

class Persona:

    nombre = ""
    apellido = ""
    edad = 0
    genero = "sin definir"

    def __init__(self, nombre, apellido, edad, genero):             #constructor

        self.nombre=nombre                            #self es como si fuera el nombre del objeto: p1, p2, etc
        self.apellido=apellido
        self.edad=edad
        self.genero=genero

    def hablar(self):

        return f"La persona que se llama {self.nombre} está hablando"
    
    def camina(self):

        return f"La persona que se llama {self.nombre} está caminando"
    
    def getDatos(self):

        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, \
Edad: {self.edad}, Genero: {self.genero}"
    

p1 = Persona("Pedro", "Lopez", 45, "Masculino")              #cada dato se pasa como argumento al constructor^

p1.nombre = "Manolo"                            #cambia el nombre de p1

p2 = Persona("Rogelio", "Periquillo", 56, "Mariquita")



print(p1.getDatos(), p1.hablar(), p1.camina())
print(p2.getDatos(), p2.hablar(), p2.camina())