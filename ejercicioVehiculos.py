class Vehiculo():
    def __init__ (self, ruedas, color, ancho, alto, marchas):
        self.ruedas = ruedas
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.marchas = marchas
        self.acelerando=False
        self.frenando=False
        self.girando=False

    def acelerar(self):
        self.acelerando=True

    def frenar(self):
        self.frenando=True

    def girar(self):
        self.girando=True

    def getDatosVehiculo(self):
        return f"El vehículo tiene {self.ruedas} ruedas, es de color {self.color}, \
tiene un ancho de {self.ancho} metros, un alto de {self.alto} metros y tiene {self.marchas} marchas."

    

class Coche(Vehiculo):

    def __init__(self, ruedas, color, ancho, alto, marchas, cilindrada, asientos, aireacondicionado):

        super().__init__(ruedas, color, ancho, alto, marchas)
        self.cilindrada = cilindrada
        self.asientos = asientos
        self.aireacondicionado = aireacondicionado

    def ir_marcha_atras(self):
        self.marcha_Atras=True

    def Arrancar(self):
        self.arrancar=True

    def getDatosVehiculo(self):
        return f"{super().getDatosVehiculo()} \
su cilindrada es de {self.cilindrada} cc y tiene {self.asientos} asientos, \
y {self.aireacondicionado} aire acondicionado."

class Furgoneta(Coche):

    def __init__(self, ruedas, color, ancho, alto, marchas, cilindrada, asientos, aireacondicionado, carga):

        super().__init__(ruedas, color, ancho, alto, marchas, cilindrada, asientos, aireacondicionado)
        self.carga = carga

    def cargar(self):
        self.cargando=True

    def descargar(self):
        self.descargando=True

    def getDatosVehiculo(self):
        return f"{super().getDatosVehiculo()}, puede cargar {self.carga}."


class Bicicleta(Vehiculo):

    def __init__(self, ruedas, color, ancho, alto, marchas):

        super().__init__(ruedas, color, ancho, alto, marchas)

    def saltar(self):
        self.saltando=True

    def derrapar(self):
        self.derrapando=True

    def getDatosVehiculo(self):
        return f"{super().getDatosVehiculo()}."

class Moto(Coche, Bicicleta):

    def __init__(self, ruedas, color, ancho, alto, marchas, cilindrada, asientos):

        super().__init__(ruedas, color, ancho, alto, marchas, cilindrada, asientos, aireacondicionado=False)

    def getDatosVehiculo(self):

        return f"{super().getDatosVehiculo()}."


coche1 = Coche(4, "rojo", 2, 1.5, 5, 2000, 5, True)
furgoneta1 = Furgoneta(4, "negro", 2, 3, 6, 3000, 5, True, 3500)
bicicleta1 = Bicicleta(2, "verde", 0.5, 0.5, 1)
moto1 = Moto(2, "azul", 0.8, 0.5, 1, 1000, 2)

print(coche1.getDatosVehiculo(), coche1.Arrancar())

print(furgoneta1.getDatosVehiculo())

print(bicicleta1.getDatosVehiculo())

print(moto1.getDatosVehiculo())