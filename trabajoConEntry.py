from tkinter import *
from tkinter import messagebox as MessageBox

raiz = Tk()                                                        # Se crea la raiz

raiz.iconbitmap("icono.ico")            # Icono de la ventana

raiz.title("Formulario")                                           # Se le pone un título a la raiz

miFrame = Frame(raiz, width=1000, height=550)                      # Se crea un frame

miFrame.pack()                                                   # Se empaqueta el frame

#----cuadros de texto-----------------------------------------------------------------------------  
# 
miVariable=StringVar()                                                # Se crea una variable de tipo string                                               

cuadroTextoNombre = Entry(miFrame, textvariable=miVariable)                                        # Se crea un cuadro de texto
cuadroTextoNombre.grid(row=0, column=1, padx=15, pady=7.5)                                   # Se crea un cuadro.row=fila, column= columna, padx=distancia horizontal, pady=distancia vertical 
cuadroTextoNombre.config(bg="yellow", fg="red", justify="right")                     # Se configura el cuadro de texto bg=color de fondo, fg=color de la letra, justify=alineación del texto

miApellido=StringVar()                                                       # Se crea un 
cuadroTextoApellido = Entry(miFrame, textvariable=miApellido)                                        # Se crea un cuadro de texto
cuadroTextoApellido.grid(row=1, column=1, padx=15, pady=7.5)                                   # Se crea un cuadro

miContraseña=StringVar()                                                    # Se crea un
cuadroTextoContraseña = Entry(miFrame, textvariable=miContraseña)                                        # Se crea un cuadro de texto
cuadroTextoContraseña.grid(row=2, column=1, padx=15, pady=7.5)
cuadroTextoContraseña.config(show="*")                                   #se ocultan las letras con un asterisco

miEmail=StringVar()                                                     # Se crea un
cuadroTextoEmail = Entry(miFrame, textvariable=miEmail)                                        # Se crea un cuadro de texto
cuadroTextoEmail.grid(row=3, column=1, padx=15, pady=7.5)                                   # Se crea un cuadro

miDireccion=StringVar()                                                     # Se crea un
cuadroTextoDireccion = Entry(miFrame, textvariable=miDireccion)                                        # Se crea un cuadro de texto
cuadroTextoDireccion.grid(row=4, column=1, padx=15, pady=7.5)                                   # Se crea un cuadro

cuadroTextoComentario = Text(miFrame, width=15, height=10)                                        # Se crea un cuadro de texto
cuadroTextoComentario.grid(row=5, column=1, padx=15, pady=7.5)                                   # Se crea un cuadro

#----scroll: para ver toda la información del cuadro de texto----------------------------------------

miScrollVertical=Scrollbar(miFrame, command=cuadroTextoComentario.yview)                        # Se crea un scroll
miScrollVertical.grid(row=5, column=2, sticky="nsew")                                            # Se crea un scroll

cuadroTextoComentario.config(yscrollcommand=miScrollVertical.set)                                # Se crea un scroll

#----labels: texto delante de los cuadros de texto-------------------------------------------------                                               

nombreLabelNombre = Label(miFrame, text="Nombre: ")                       # Se crea una etiqueta
nombreLabelNombre.grid(row=0, column=0, sticky="e")                        #grid es un método que permite organizar los widgets en filas y columnas y sticky="w" alinea el texto a la izquierda. w=west (oeste)                                                                       

nombreLabelApellido = Label(miFrame, text="Apellido: ")                       # Se crea una etiqueta
nombreLabelApellido.grid(row=1, column=0, sticky="e")  

nombreLabelContraseña = Label(miFrame, text="Contraseña: ")                       # Se crea una etiqueta
nombreLabelContraseña.grid(row=2, column=0, sticky="e") 

nombreLabelEmail = Label(miFrame, text="Email: ")                       # Se crea una etiqueta
nombreLabelEmail.grid(row=3, column=0, sticky="e") 

nombreLabelDireccion = Label(miFrame, text="Dirección: ")                       # Se crea una etiqueta
nombreLabelDireccion.grid(row=4, column=0, sticky="e")

nombreLabelComentario = Label(miFrame, text="Comentario: ")                       # Se crea una etiqueta
nombreLabelComentario.grid(row=5, column=0, sticky="e")

#----botones----------------------------------------------------------------------------------------
#variables=[miVariable, miApellido, miContraseña, miEmail, miDireccion]
#Datos=[]
def funcionBoton():                                                                 # Se crea una función

    cuadroTextoComentario.insert(INSERT, "VIva yo")

    #MessageBox.showinfo("Datos: ", "\n".join(var.get() for var in variables))

    #Datos.extend(var.get() for var in variables)

    #print(Datos)

                        

BotonEnviar = Button(raiz, text="Enviar", bg="pink", command=funcionBoton)                                     # Se crea un botón

BotonEnviar.pack()                                                          # Se empaqueta el botón




raiz.mainloop()