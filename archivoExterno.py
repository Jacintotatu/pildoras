from io import open
"""
archivo_externo= open("primerarchivo.txt", "w")

archivo_externo.write("Bienvenido a los archivos externos")

archivo_externo.close()

print("Archivo creado con éxito")

print("-------------------------------")

archivo_externo = open("primerarchivo.txt", "a")

archivo_externo.write("\nGuardamos informacion de forma permanente")

archivo_externo.close()

print("Información añadida al archivo con éxito")


archivo_externo = open("primerarchivo.txt", "r")             #r : read 

#informacion = archivo_externo.read()      #read() : lee todo el archivo

#informacion = archivo_externo.readline()  #readline() : lee la primera línea del archivo

informacion = archivo_externo.readlines()  #readlines() : lee todas las líneas del archivo

archivo_externo.close()

print(informacion[0])        # imprime la segunda línea del archivo

print("-------------------------------")
"""
archivo_externo = open("primerarchivo.txt", "a")

#archivo_externo.write("\nAgregamos más información al archivo")

archivo_externo.close()

#print("Información añadida al archivo con éxito")

#intentamos borrar la ultima linea del archivo
archivo_externo = open("primerarchivo.txt", "r")               #r : read

informacion = archivo_externo.readlines()               #readlines() : lee todas las líneas del archivo

archivo_externo.close()                  #close() : cierra el archivo

informacion.pop()                     #pop() : elimina el último elemento de la lista

archivo_externo = open("primerarchivo.txt", "w")         #w : write

archivo_externo.writelines(informacion)                 #writelines() : escribe una lista de líneas en el archivo

archivo_externo.close()                 #close() : cierra el archivo 

print(informacion)                   #imprime la lista sin el último elemento


