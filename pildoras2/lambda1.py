Area_Cuadrado = lambda base, altura: base*altura
"""
Este script contiene funciones lambda para calcular las áreas de diferentes figuras geométricas:
- Cuadrado/Rectángulo
- Círculo
- Triángulo
Funciones:
- Area_Cuadrado(base, altura): Calcula el área de un cuadrado o rectángulo dada su base y altura.
- Area_Circulo(radio): Calcula el área de un círculo dado su radio.
- Area_Triangulo(base, altura): Calcula el área de un triángulo dada su base y altura.
Ejemplo de uso:
- Area_Cuadrado(5, 10) devuelve 50
- Area_Circulo(10) devuelve 314.0
- Area_Triangulo(5, 8) devuelve 20.0
"""

print(f"El area del cuadrado son {Area_Cuadrado(5, 10)} cm")

Area_Circulo = lambda radio: 3.14*radio**2                                      

print(Area_Circulo(10))

Area_Triangulo = lambda base, altura: (base*altura)/2

print(Area_Triangulo(5, 8))

 