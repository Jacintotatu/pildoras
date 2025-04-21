from tkinter import *

from Operaciones_Calculadora import *

def construir_Botones(self, botones, filas_botones):                                                                  

    contador=0

    for fila in range(2,filas_botones+2):                                                                                     # Se crean los botones
        for columna in range(4):
            botones[contador].grid(row=fila, column=columna)
            contador+=1                                                                                             # Se crean los botones

def colocar_Boton(self, valor,mostrar=True, ancho=9, alto=1):                                                             # Se crea la función para colocar los botones
    return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 9),
    command=lambda:pulsaciones_teclas(self, valor, mostrar))