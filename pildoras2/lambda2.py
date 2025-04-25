"""
mi_lista=[(4, 6), (2, 3), (1, 2), (5, 7), (8, 9)]

mi_lista.sort(key=lambda t: t[0]+t[1])

print(mi_lista)
"""

musicos = ["Jimi Hendrix", "Eric Clapton", "Jimmy Page", "Keith Richards", "Chuck Berry", "B.B. King", "Stevie Ray Vaughan", "Carlos Santana", "David Gilmour", "Mark Knopfler"]

musicos.sort(key=lambda musico:musico.split()[1])

print(musicos)