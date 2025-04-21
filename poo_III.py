class Persona:

    __nombre = ""
    apellido = ""
    __edad = 0
    genero = "sin definir"

    def __init__(self, nombre, apellido, genero):             #constructor

        self.__nombre=nombre                            #self es como si fuera el nombre del objeto: p1, p2, etc
        self.apellido=apellido

        self.genero=genero

    def setEdad(self, laEdad):                      #setters
        if laEdad<0 or laEdad>100:
            print("Error en la edad")
         
        else:
            self.__edad=laEdad
            return self.__edad


    def hablar(self):

        return f"La persona que se llama {self.__nombre} está hablando"
    
    def camina(self):

        return f"La persona que se llama {self.__nombre} está caminando"
    
    def getDatos(self):                                                     #getters

        return f"Nombre: {self.__nombre}, Apellido: {self.apellido}, \
Edad: {self.__edad}, Genero: {self.genero}"
    

p1 = Persona("Pedro", "Lopez","Masculino")              #cada dato se pasa como argumento al constructor^

p1.__nombre = "Manolo"                            #con __ ya no se cambia el nombre de p1

p2 = Persona("Rogelio", "Periquillo", "Mariquita")

p1.setEdad(125)                                 #el if del setters impide que se agregue ese valor

p2.setEdad(34)                                        #cambia la edad de p1

print(p1.getDatos())
print(p2.getDatos())