frases=["Los lunes son los mejores dias para programar", "Python es moderno", "Veremos inteligencia artificial mas adelante", 
        "Lambda simplifica el código"]

frases.sort (key= lambda x:len(x.split()), reverse=True)

print(frases)
