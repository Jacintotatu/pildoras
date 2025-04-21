import sys
edad = input("Introduce tu edad: ")

contador = 1

while edad.isdigit()== False:

    print("El valor introducido no es correcto")

    edad = input("Introduce tu edad: ")

    contador += 1
    
    if contador == 3:

        print("Has superado el numero de intentos permitidos")

        sys.exit()                                #sale del programa sin error

if int(edad)<18:

    print("No puedes pasar")

else:

    print("Puedes pasar")

