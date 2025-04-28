def funcion_decoradora(funcion_parametro):                                       # Decoradora

    def funcion_interna():                                                       # Función interna

        print("A continuacion voy a realizar un cálculo")

        funcion_parametro()

        print("He terminado de realizar el cálculo")

    return funcion_interna



@funcion_decoradora
def suma():
    print(5 + 5)

@funcion_decoradora
def resta():
    print(5 - 5)

suma()
resta()