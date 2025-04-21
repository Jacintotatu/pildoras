class Coche:
    ruedas=4
    largoChasis=260
    anchoChasis=150
    arrancado = False           # version 2 del video 32
    def arrancar(self):           #método o comportamiento
        #pass
        self.arrancado = True

    def estadoCoche(self):
        if self.arrancado:
            return "El coche está arrancado"
        else:
            return "El coche está parado"

mazda = Coche()                  #ejemplares de clase
renault = Coche()
print(f"Tu coche tiene {renault.ruedas} ruedas")
renault.arrancar()                                       #se ha arrancado el coche
print(f"El coche Renault está arrancado? {renault.arrancado}")
print(f"Como esta el mazda? {mazda.estadoCoche()}")         #el coche no se ha arrancado todavía
print(f"Como esta el renault? {renault.estadoCoche()}")
