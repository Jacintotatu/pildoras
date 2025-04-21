class CuentaCorriente():

    def __init__(self, numero, titular, saldo):
        
        self.numero=numero
        self.titular=titular
        self.saldo=saldo

    def getDatosPersona(self):
        
        return f"La cuenta número {self.numero} es de {self.titular} y tiene un saldo de {self.saldo}"
    
    def ingresar(self, cantidad):
        self.saldo += cantidad
        return self.saldo
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return "No hay saldo suficiente"
        else:
            self.saldo -= cantidad
            return self.saldo
        

cuenta1 = CuentaCorriente("3895","Perico Perez", 1200)

cuenta1.ingresar(450)

print(cuenta1.getDatosPersona())

cuenta1.retirar(378)

print(cuenta1.getDatosPersona())