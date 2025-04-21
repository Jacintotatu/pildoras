class Persona():

    def __init__(self, nombre, apellido, edad):

        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def getDatosPersonales(self):           #getters

        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}"
    
    def habla(self):

        return "La persona está hablando"
    
    def piensa(self):

        return "La persona está pensando"
    
    def camina(self):

        return "La persona está caminando"
    
    def come(self):

        return "La persona está comiendo"
        
persona1 = Persona("Ana", "Gomez", 35)


class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, escuela):
        Persona.__init__(self,nombre, apellido, edad)                          #con super() se llama al constructor de la clase padre
        #super se sustituye por el nombre de la clase padre
        
        self.escuela=escuela                                            #se agrega el atributo escuela

    def estudia(self):

        return "Estoy estudiando"
    
    def getDatosPersonales(self):

        return f"{super().getDatosPersonales()}, Escuela: {self.escuela}"              #se llama al metodo getDatosPersonales de la clase padre con super()
    



class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa):
        
        Persona.__init__(self,nombre, apellido, edad)                    #con super() se llama al constructor de la clase padre
        #super se sustituye por el nombre de la clase padre
        self.empresa=empresa                                         #se agrega el atributo empresa

    def trabaja(self):

        return "Estoy trabajando"
    
    def getDatosPersonales(self):

        return f"{super().getDatosPersonales()}, Empresa: {self.empresa}"              #se llama al metodo getDatosPersonales de la clase padre con super()

class Director(Trabajador, Estudiante):

    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):

        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)
        self.bonus=bonus

    def getDatosPersonales(self):
        return f"{super().getDatosPersonales()} Bonus: {self.bonus}"
    
    def dirige(self):

        return "Estoy dirigiendo"
    

trabajador1 = Trabajador("Pedro", "Ruiz", 47, "Imasa")
persona1 = Persona("Ana", "Gomez", 35)
estudiante1 = Estudiante("Juan", "Diaz", 21, "Nuestra señora.") 
director1 = Director("Rogelio", "Martin", 56, "Farmacia", "Carmelitas", 2000)

print(persona1.getDatosPersonales(), persona1.habla())
print(estudiante1.getDatosPersonales(), estudiante1.estudia())
print(trabajador1.getDatosPersonales(), trabajador1.trabaja())
print(director1.getDatosPersonales(), director1.dirige())
