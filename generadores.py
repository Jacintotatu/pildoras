"""
def generarPares (limite):

    num = 1

    numerosPares = []

    while num < limite:

        numerosPares.append(num*2)

        num += 1

    return numerosPares


print(generarPares(10))
"""

def generarPares(limite):

    num = 1

    while num < limite:

        yield num * 2

        num += 1

sucesionPares = generarPares(6)

#for i in sucesionPares:      #imprime los números pares en un bucle for de una vez

    #print(i)

print(next(sucesionPares))     # Imprime el primer número par

print("venga otro numero")      

print(next(sucesionPares))     # Imprime el segundo número par

print("venga otro numero")

print(next(sucesionPares))     # Imprime el tercer número par

print("venga otro numero")

print(next(sucesionPares))

print("venga otro numero")

print(next(sucesionPares))

print("venga otro numero")