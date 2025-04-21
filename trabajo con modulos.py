#import funciones_matematicas                      # Importamos el modulo funciones_matematicas

#funciones_matematicas.sumar(7,5)                     

#funciones_matematicas.restar(10,3)

#funciones_matematicas.multiplicar(3,7)

#-------------------------------------------------------------

#from funciones_matematicas import sumar, restar                   # Importamos solo las funciones sumar y restar del modulo funciones_matematicas

#sumar(7,5)                                # Llamamos a la funcion sumar

#restar(10,3)                              # Llamamos a la funcion restar


#-------------------------------------------------------------

from moduloMatematico.calculosBasicos.funciones_matematicas import *                            # Importamos todas las funciones del modulo funciones_matematicas
#from moduloMatematico.otrosCalculos.PotenciaYRedondeo import *                            # Importamos todas las funciones del modulo potenciaYRedondeo
                                                                                            #desde la carpeta (paquete) moduloMatematico
sumar(7,5)                                # Llamamos a la funcion sumar

restar(10,3)                              # Llamamos a la funcion restar

multiplicar(3,7)                            # Llamamos a la funcion multiplicar

#potencia(2,3)                            # Llamamos a la funcion potencia

#redondear(12.75)                            # Llamamos a la funcion redondear