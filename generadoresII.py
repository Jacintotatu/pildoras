def capitales_mundo(*ciudades):

    #for capital in ciudades:     #DEVUELVE CIUDAD UNA A UNA
        #yield capital

    #for capital in ciudades:
        #for letra_capital in capital:    #DEVUELVE letras DE LA CIUDAD UNA A UNA
            #yield letra_capital

    for capital in ciudades:
        yield from capital                 # y esto devuelve lo mismo

# Test the function

capitales_devueltas= capitales_mundo('Madrid', 'London', 'Paris', 'Berlin', 'Rio de Janeiro')

print(next(capitales_devueltas))  # Output:  

print(next(capitales_devueltas))  # Output:  

print(next(capitales_devueltas))  # Output: 