from tkinter import *

root = Tk()                                     # Crear la ventana, primer contenedor 

miFrame=Frame(root, width=700, height=650)      # Crear un Frame, segundo contenedor, contenedorpadre del frame

miFrame.pack()                                 # Añadir el Frame a la ventana

#miLabel=Label(miFrame, text="Hoy son los santos inocentes")                  # Crear un Label, tercer contenedor, contenedor padre del label

#miLabel.place(x=120, y=125)                                                          # place() = colocar el Label en el Frame. pixels 

#Label(miFrame, text="Hoy son los santos inocentes", fg="blue", font=("Courier", 20)).place(x=120, y=125)           # Crear:texto + fg + font  y colocar: place = el Label en el Frame

miLogo=PhotoImage(file="archivo.png")           # Crear un Label, con imagen

Label(miFrame, image=miLogo).place(x=0,y=0)    # Crear y colocar el Label en el Frame



root.mainloop()                                # Bucle infinito de la ventana