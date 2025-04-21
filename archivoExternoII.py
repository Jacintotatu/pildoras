import os

import io

#os.makedirs("pruebaDirectorio")                     # Crea un directorio

os.chdir("pruebaDirectorio")                       # Cambia al directorio creado    

archivoDirectorio = open("incluido.txt", "w")               # Crea un archivo en el directorio

archivoDirectorio.write("Espero que salga bien")  # Escribe en el archivo

archivoDirectorio.close()                       # Cierra el archivo

print(os.getcwd()) # Imprime el directorio actual

print(os.listdir("./"))         # Imprime el contenido del directorio a modo de lista

os.chdir("..")                   # Cambia al directorio anterior



os.chdir("moduloMatematico") # Cambia al directorio

print(os.getcwd()) # Imprime el directorio actual

#os.makedirs("prueba")

lista = os.listdir("./")               # Imprime el contenido del directorio a modo de lista

for i in lista:
    print(i)
    
print(lista)

os.chdir("prueba") # Cambia al directorio


print(os.getcwd()) # Imprime el directorio actual

archivoPrueba = open("pelagatos.txt", "w")          # Crea un archivo en el directorio

archivoPrueba.write("Pelagatos como tres peces") # Escribe en el archivo

archivoPrueba.close()                       # Cierra el archivo

archivoPrueba = open("pelagatos.txt", "r")           # Abre el archivo en modo lectura

archivoPrueba.seek(2)                # Mueve el cursor al segundo caracter

print(archivoPrueba.read())             # Imprime el contenido del archivo









