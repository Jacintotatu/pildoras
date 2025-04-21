from tkinter import *
import re

raiz=Tk()                                                                                                                # Se crea la raiz

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self. ventana.title("Calculadora POO")                                                                           # Se le da un título a la ventana
        self.operacion=""

        self.display=Entry(ventana, font="Arial 15")                                                                     # Se crea un cuadro de texto para el display

        #ubicar Display

        self.display.grid(row=1, column=0, columnspan=4, pady=10)                                                #colspan ocupa 4 columnas y rowspan ocupa 1 fila
        self.display.config(bg="darkgreen", bd=5, font=("Arial 20"), fg="lightgreen", justify="right", width=15)          # Se configura el cuadro de texto

        #Agregar botones

        boton7=self.colocar_Boton(7)                                                                                      # Se crean los botones
        boton8=self.colocar_Boton(8)                                                                                      # Se crean los botones
        boton9=self.colocar_Boton(9)                                                                                      # Se crean los botones
        botondiv=self.colocar_Boton("/")                                                                                      # Se crean los botones
#-------------------------------------------------------
        boton4=self.colocar_Boton(4)                                                                                      # Se crean los botones
        boton5=self.colocar_Boton(5)                                                                                      # Se crean los botones
        boton6=self.colocar_Boton(6)                                                                                      # Se crean los botones
        botonmult=self.colocar_Boton(u"\u00D7")# Se crean los botones
#-------------------------------------------------------
        boton1=self.colocar_Boton(1)                                                                                      # Se crean los botones
        boton2=self.colocar_Boton(2)                                                                                      # Se crean los botones
        boton3=self.colocar_Boton(3)                                                                                      # Se crean los botones
        botonrest=self.colocar_Boton("-")                                                                  # Se crean los botones
#-------------------------------------------------------
        boton0=self.colocar_Boton(0)                                                                                      # Se crean los botones
        botoncoma=self.colocar_Boton(".")                                                                                      # Se crean los botones
        botonigual=self.colocar_Boton("=", mostrar=False)                                                                                      # Se crean los botones
        botonmas=self.colocar_Boton("+")                                                                  # Se crean los botones 
#-------------------------------------------------------
        botones=[boton7, boton8, boton9, botondiv, boton4, boton5, boton6, botonmult, boton1, boton2, boton3, botonrest, boton0, botoncoma, botonigual, botonmas]      

        contador=0

        for fila in range(2,6):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador+=1                                                                                             # Se crean los botones

    def colocar_Boton(self, valor,mostrar=True, ancho=9, alto=1):                                                             # Se crea la función para colocar los botones
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 9),
        command=lambda:self.pulsaciones_teclas(valor, mostrar))
    
    def pulsaciones_teclas(self, valor, mostrar):                                                                   # Se crea la función para las pulsaciones de los botones
        
        if mostrar:
            self.operacion+=str(valor)                                                                                  # Se añade el valor a la operación
            self.mostrar_pantalla(valor)
        elif not mostrar and valor=="=":
            self.operacion=re.sub(u"\u00D7", "*", self.operacion)                                                                                  # Se sustituye el valor de la multiplicación por el de la división
            self.borrar_pantalla()
            self.mostrar_pantalla(str(eval(self.operacion)))                                                                                  # Si el valor es igual se evalua la operación. Eval evalua la operación y devuelve el resultado
        else:
            pass

    def mostrar_pantalla(self, valor):                                                                                  # Se crea la función para mostrar el texto en el display
        self.display.insert(END, valor)                                                                                  # Se inserta el valor en el display

    def borrar_pantalla(self):                                                                                         # Se crea la función para borrar el display
        self.display.delete(0, END)                                                                                     # Se borra el display


mi_calculadora=Calculadora(raiz)                                                                                          #instancia de la clase calculadora
raiz.mainloop()                                                                                                           #inicia el bucle de la ventana
