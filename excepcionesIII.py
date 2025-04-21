def divide():

    try:

        op1 = float(input("Introduce el primer numero: "))
        op2 = float(input("Introduce el segundo numero: "))

        print(f"El resultado de la division es: {op1 / op2}")

    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    except ValueError:
        print("Los valores introducidos no son correctos")

    finally:
        print("Se ha intentado ejecutar la función en su totalidad")

divide()

print("Cálculo finalizado")
