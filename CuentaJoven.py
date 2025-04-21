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
        

class CuentaJoven(CuentaCorriente):
    
        def __init__(self, numero, titular, saldo, bonus_promocion):
            super().__init__(numero, titular, saldo)
            self.bonus_promocion=bonus_promocion
    
        def getDatosPersona(self):
            
            return f"{super().getDatosPersona()} y tiene una bonificación de {self.bonus_promocion}"
        
        def bonificacion(self):
            self.saldo += self.bonus_promocion
            return self.saldo
    

c1 = CuentaJoven("12345", "Perico Pelao", 5000, 250)


c1.ingresar(1000)
c1.bonificacion()
c1.retirar(600)

print(c1.getDatosPersona())
   
   