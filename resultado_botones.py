from tkinter import *


def mostrar_pantalla(self, valor):                                                                                  # Se crea la función para mostrar el texto en el display
    self.display.insert(END, valor)                                                                                  # Se inserta el valor en el display

def borrar_pantalla(self):                                                                                         # Se crea la función para borrar el display
    self.display.delete(0, END)                                                                                     # Se borra el display

