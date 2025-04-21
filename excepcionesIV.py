import math

def calculaRaizCuadrada(numero):

    if numero < 0:
        raise ValueError("El número no puede ser negativo")   #raise : personaliza el mensaje de error y obliga al programador a crear un bloque try except
    
    else:
        return math.sqrt(numero)  # return : devuelve el resultado al programa principal
    
numeroUsuario = (int(input("Introduce un número: ")))   # input : permite al usuario introducir un dato al programa

try: 
    print(calculaRaizCuadrada(numeroUsuario))    # calculaRaizCuadrada : calcula la raíz cuadrada del número

except ValueError:
    print("Error: El número introducido no puede ser negativo")     # ValueError : mensaje de error personalizado para el caso de un número negativo

print("Y por aqui continuaria el programa")     
