
"""
mi mierda que yo hice
listaNombres=[]

contador=1

while contador <= 10:
    nombre=input("Introduce un nombre: ")

    if nombre in listaNombres:


        
        raise ValueError ("El nombre ya existe en la lista")

        continue
        
        
    else:
        listaNombres.append(nombre)
        contador += 1
        

for i in listaNombres:
    print(i)       
"""
#la buena

nombresPersonas = []

def agregar_a_lista(lista, nombreIntroducido):

    try: 
        if nombreIntroducido in lista:
            raise ValueError
        else:
            lista.append(nombreIntroducido)

    except ValueError:
        print(f"Error, {nombreIntroducido} ya se ha introducido")

introducidos = 1

while introducidos <= 10:

    nombre = input("Introduce un nombre: ")
    agregar_a_lista(nombresPersonas, nombre)
    introducidos += 1

for nombre in nombresPersonas:

    print(nombre)