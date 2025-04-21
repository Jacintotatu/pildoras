#__repr__

import datetime

hoy=datetime.date.today()

print(hoy)                 

print(str(hoy))                   #imprime tal cual, como el print solo


print(repr(hoy))                   #mas preciso


#__len__

class Agenda():                  

    def __init__(self):              #

        self.miAgenda = {}

    def agregarPersonas(self, nombre, telefono):                              

        self.miAgenda[nombre]=telefono        

    def obtenerContactos(self):              

        return self.miAgenda.items()

    def __len__(self):                       

        return len(self.miAgenda)
    
agendaPersonal=Agenda()


agendaPersonal.agregarPersonas("Juan", "1234567")
agendaPersonal.agregarPersonas("Ana", "7654321")
agendaPersonal.agregarPersonas("Pedro", "12342567")
agendaPersonal.agregarPersonas("Juani", "124567")
agendaPersonal.agregarPersonas("Antonio", "654321")
agendaPersonal.agregarPersonas("Pepe", "1232567")

print(len(agendaPersonal))

for nombre, telefono in agendaPersonal.obtenerContactos():

    print(f"{nombre} : {telefono}")







