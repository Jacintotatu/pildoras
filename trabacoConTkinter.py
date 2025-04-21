from tkinter import *

raiz = Tk()                                     # Crear la ventana

raiz.title("Primera Ventana Python")                      # Titulo de la ventana    

raiz.resizable(1,1)                    # con (0,0) No permite redimensionar la ventana      

raiz.iconbitmap("icono.ico")            # Icono de la ventana

raiz.geometry("700x400")                # Tamaño de la ventana

raiz.config(bg="green")                  # Color de fondo de la ventana

miFrame = Frame()                       # Crear un Frame

#miFrame.pack(side="right", anchor="s")                        # Alineacion del Frame

#miFrame.pack(fill="y", expand="True")                  # Alineacion del Frame

miFrame.pack(fill="both", expand="True")                  # Alineacion del Frame

miFrame.config(bg="red")                 # Color de fondo del Frame

miFrame.config(width="650", height="350")                # Tamaño del Frame


raiz.mainloop()                                        # Bucle infinito de la ventana



