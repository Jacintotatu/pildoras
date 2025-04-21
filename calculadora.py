from tkinter import *

raiz=Tk()                                                                      # Se crea la raiz

raiz.iconbitmap("icono.ico")                                                   # Icono de la ventana   

raiz.title("Calculadora")                                                      # Título de la ventana

frampant=Frame(raiz, width=400, height=500, bg="darkgrey")                     # Se configura el frame

frampant.pack()                                                                # Se empaqueta el frame

misBotones = Frame(raiz, width=400, height=500, bg="darkgrey")                 # Se configura el frame

misBotones.pack()                                                              # Se empaqueta el frame

#----operaciones---------------------------------------------------------

operacion=""
resultado=0
ultima_operacion = ""  # Nueva variable para rastrear la última operación

#entry--------pantalla--------------------------------------------------------

miPantalla=StringVar(value="0")

pantalla = Entry(frampant, textvariable=miPantalla)                               # Se crea un cuadro de texto

pantalla.grid(row=0, column=0, padx=5, pady=5)

pantalla.config(bg="darkgreen", bd=5, font=("Arial 20"), fg="lightgreen", justify="right")          # Se configura el cuadro de texto


#pulsaciones numeros---------------------------------------------------------

def pulsacionesTeclas(numPulsado):
    global operacion
    current_value = miPantalla.get()
    if operacion != "":  # Si hay una operación previa
        miPantalla.set(numPulsado)  # Reemplaza el valor actual
        operacion = ""
    elif current_value == "0":  # Si el valor actual es 0
        miPantalla.set(numPulsado)  # Reemplaza el 0
    else:
        miPantalla.set(current_value + numPulsado)  # Añade el número pulsado


# Función para manejar la coma----------------------------------------------
def repetirComa(tecla):
    current_value = miPantalla.get()  # Obtiene el valor actual de la pantalla
    if "," not in current_value:  # Solo permite una coma
        miPantalla.set(current_value + tecla)  # Añade la coma al valor actual
# Funcion suma---------------------------------------------------------------

def suma(num):
    global operacion, resultado, ultima_operacion
    num = num.replace(",", ".")  # Reemplaza la coma por punto
    if resultado == 0:  # Si es la primera operación
        resultado = float(num)
    else:
        resultado += float(num)
    operacion = "suma"
    ultima_operacion = "suma"
    # Mantén el formato original del número (sin decimales si es entero)
    if resultado.is_integer():
        miPantalla.set(str(int(resultado)))
    else:
        miPantalla.set(str(resultado).replace(".", ","))
# Funcion resta---------------------------------------------------------------

def resta(num):
    global operacion, resultado, ultima_operacion
    num = num.replace(",", ".")  # Reemplaza la coma por punto
    if resultado == 0:  # Si es la primera operación
        resultado = float(num)
    else:
        resultado -= float(num)
    operacion = "resta"
    ultima_operacion = "resta"
    # Mantén el formato original del número (sin decimales si es entero)
    if resultado.is_integer():
        miPantalla.set(str(int(resultado)))
    else:
        miPantalla.set(str(resultado).replace(".", ","))

# Funcion multiplicacion---------------------------------------------------------------

#def multi(num):
   # global operacion
    #global resultado
    #resultado*=int(num)
    #operacion = "multiplicacion"
    #miPantalla.set(resultado)


#funcion total---------------------------------------------------------------

def total():
    global resultado, operacion, ultima_operacion
    num = miPantalla.get().replace(",", ".")  # Reemplaza la coma por punto
    
    if ultima_operacion == "suma":
        resultado += float(num)
    elif ultima_operacion == "resta":
        resultado -= float(num)
    
    # Mantén el formato original del número (sin decimales si es entero)
    if resultado.is_integer():
        miPantalla.set(str(int(resultado)))
    else:
        miPantalla.set(str(resultado).replace(".", ","))
    
    operacion = ""
    ultima_operacion = ""  # Resetea la última operación




#alernativa para botones con tuplas------------------------------------------

"""
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("x", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
    (",", 4, 0), ("0", 4, 1), ("=", 4, 2), ("-", 4, 3)                          # Se define una lista de tuplas con los botones y sus posiciones en row y column
]

# Creación y colocación de los botones
for (texto, fila, columna) in botones:                                                  # Se itera sobre la lista de botones
    if texto == ",":                                                                    # Si el texto es una coma se crea un botón diferente
        boton = Button(misBotones, text=texto, width=9, height=3, bg="darkgrey", command=lambda t=texto: repetirComa(t))                            # Se crea un botón
    else:
        boton = Button(misBotones, text=texto, width=9, height=3, bg="darkgrey", command=lambda t=texto: pulsacionesTeclas(t))                      # Se crea un botón
        boton.grid(row=fila, column=columna, padx=1, pady=1)                                                                                        # Se coloca el botón en la cuadrícula

"""

#botones------fila 1--------------------------------------------------------


boton7=Button(misBotones, text="7", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("7"))                          # Se crea un botón

boton7.grid(row=1, column=0, padx=1, pady=1)


boton8=Button(misBotones, text="8", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("8"))                          # Se crea un botón

boton8.grid(row=1, column=1, padx=1, pady=1)


boton9=Button(misBotones, text="9", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("9"))                          # Se crea un botón

boton9.grid(row=1, column=2, padx=1, pady=1)


botonDiv=Button(misBotones, text="/", width=9, height=3, bg="darkgrey",)                          # Se crea un botón

botonDiv.grid(row=1, column=3, padx=1, pady=1)


#botones------fila 2--------------------------------------------------------


boton4=Button(misBotones, text="4", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("4"))                          # Se crea un botón

boton4.grid(row=2, column=0, padx=1, pady=1)


boton5=Button(misBotones, text="5", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("5"))                          # Se crea un botón

boton5.grid(row=2, column=1, padx=1, pady=1)


boton6=Button(misBotones, text="6", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("6"))                          # Se crea un botón

boton6.grid(row=2, column=2, padx=1, pady=1)  


botonX=Button(misBotones, text="x", width=9, height=3, bg="darkgrey", command=lambda:multi(miPantalla.get()))                          # Se crea un botón

botonX.grid(row=2, column=3, padx=1, pady=1) 


#botones------fila 3--------------------------------------------------------


boton1=Button(misBotones, text="1", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("1"))                          # Se crea un botón

boton1.grid(row=3, column=0, padx=1, pady=1)


boton2=Button(misBotones, text="2", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("2"))                          # Se crea un botón

boton2.grid(row=3, column=1, padx=1, pady=1)  


boton3=Button(misBotones, text="3", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("3"))                          # Se crea un botón

boton3.grid(row=3, column=2, padx=1, pady=1)  


botonSum=Button(misBotones, text="+", width=9, height=3, bg="darkgrey", command=lambda:suma(miPantalla.get()))                          # Se crea un botón

botonSum.grid(row=3, column=3, padx=1, pady=1)


#botones------fila 4--------------------------------------------------------


botonComa=Button(misBotones, text=",", width=9, height=3, bg="darkgrey", command=lambda:repetirComa(","))                          # Se crea un botón

botonComa.grid(row=4, column=0, padx=1, pady=1)


boton0=Button(misBotones, text="0", width=9, height=3, bg="darkgrey", command=lambda:pulsacionesTeclas("0"))                          # Se crea un botón

boton0.grid(row=4, column=1, padx=1, pady=1)  


botonIgual=Button(misBotones, text="=", width=9, height=3, bg="darkgrey", command=lambda:total())                          # Se crea un botón

botonIgual.grid(row=4, column=2, padx=1, pady=1) 


botonRes=Button(misBotones, text="-", width=9, height=3, bg="darkgrey", command=lambda:resta(miPantalla.get()))                          # Se crea un botón

botonRes.grid(row=4, column=3, padx=1, pady=1)



raiz.mainloop()                                                                # Se inicia el bucle de la ventana

