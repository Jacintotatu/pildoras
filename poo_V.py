class Persona():

    def hablar(self):

        return "Hablo como una persona"
    
class Trabajador(Persona):

    def hablar(self):

        return "Hablo como un trabajador"
    
    
class Director(Trabajador):

    def hablar(self):

        return "Hablo como un director"
    
#def hazlesHablar(listaDeLasPersonas):

    #for persona in listaDeLasPersonas:
        #print(persona.hablar())

def hazlesHablar(objeto):

    print(objeto.hablar())


Antonio = Persona()
Maria = Trabajador()
Ana = Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

print("----------------------------------------------------")

#listaDePersonas = [Antonio, Maria, Ana]

#hazlesHablar(listaDePersonas)

hazlesHablar(Antonio)
hazlesHablar(Maria)
hazlesHablar(Ana) 