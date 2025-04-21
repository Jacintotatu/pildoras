from tkinter import *

from Botonera_Calculadora import construir_Botones, colocar_Boton                                                                                              # Se importa el archivo Botonera_Calculadora
from Operaciones_Calculadora import *                                                                                          # Se importa el archivo Operaciones_Calculadora
from resultado_botones import *                                                                                               # Se importa el archivo resultado_botones 

# Se importa el archivo Operaciones_Calculadora
raiz=Tk()                                                                                                                # Se crea la raiz

class Calculadora:
        def __init__(self, ventana):
                self.ventana = ventana
                self. ventana.title("Calculadora modulos")                                                                           # Se le da un título a la ventana
                self.operacion=""

                self.display=Entry(ventana, font="Arial 15")                                                                     # Se crea un cuadro de texto para el display

        #ubicar Display,

                self.display.grid(row=1, column=0, columnspan=4, pady=10)                                                #colspan ocupa 4 columnas y rowspan ocupa 1 fila
                self.display.config(bg="darkgreen", bd=5, font=("Arial 20"), fg="lightgreen", justify="right", width=15)          # Se configura el cuadro de texto

        #Agregar botones
#fila1------------------------------------------------------    

                boton7=colocar_Boton(self, 7)                                                                                      # Se crean los botones
                boton8=colocar_Boton(self,8)                                                                                      # Se crean los botones
                boton9=colocar_Boton(self,9)                                                                                      # Se crean los botones
                botondiv=colocar_Boton(self,"/")                                                                                      # Se crean los botones
#fila2-------------------------------------------------------
                boton4=colocar_Boton(self,4)                                                                                      # Se crean los botones
                boton5=colocar_Boton(self,5)                                                                                      # Se crean los botones
                boton6=colocar_Boton(self,6)                                                                                      # Se crean los botones
                botonmult=colocar_Boton(self, u"\u00D7")# Se crean los botones
#fila3-------------------------------------------------------
                boton1=colocar_Boton(self,1)                                                                                      # Se crean los botones
                boton2=colocar_Boton(self,2)                                                                                      # Se crean los botones
                boton3=colocar_Boton(self,3)                                                                                      # Se crean los botones
                botonrest=colocar_Boton(self,"-")                                                                  # Se crean los botones
#fila4-------------------------------------------------------
                boton0=colocar_Boton(self,0)                                                                                      # Se crean los botones
                botoncoma=colocar_Boton(self,".")                                                                                      # Se crean los botones
                botonigual=colocar_Boton(self,"=", mostrar=False)                                                                                      # Se crean los botones
                botonmas=colocar_Boton(self,"+")                                                                  # Se crean los botones 
#prueba de añadir fila-------------------------------------------------------

                #botonq=colocar_Boton(self,"q")                                                                                      # Se crean los botones
                #botonw=colocar_Boton(self,"w")                                                                                      # Se crean los botones
                #botone=colocar_Boton(self,"e")                                                                                      # Se crean los botones
                #botonr=colocar_Boton(self,"r") 
        
                botones=[boton7, boton8, boton9, botondiv, boton4, boton5, boton6, botonmult, boton1, boton2, boton3, botonrest, boton0, botoncoma, botonigual, botonmas]
                construir_Botones(self, botones, 4)


mi_calculadora=Calculadora(raiz)                                                                                          #instancia de la clase calculadora
raiz.mainloop()                                                                                                           #inicia el bucle de la ventana
