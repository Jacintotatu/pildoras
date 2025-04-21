from tkinter import *
import re

from resultado_botones import *

def pulsaciones_teclas(self, valor, mostrar):                                                                   # Se crea la función para las pulsaciones de los botones
        
    if mostrar:
        self.operacion+=str(valor)                                                                                  # Se añade el valor a la operación
        mostrar_pantalla(self,valor)
    elif not mostrar and valor=="=":
        self.operacion=re.sub(u"\u00D7", "*", self.operacion)                                                                                  # Se sustituye el valor de la multiplicación por el de la división
        borrar_pantalla(self)
        mostrar_pantalla(self,str(eval(self.operacion)))                                                                                  # Si el valor es igual se evalua la operación. Eval evalua la operación y devuelve el resultado
    else:
        pass