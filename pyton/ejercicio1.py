#1. Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.
#

#declarar variables
calificacion_1 = 0
calificacion_2 = 0
calificacion_3 = 0

#entrada
calificacion_1 = float(input("ingrese la calificacion 1:\n"))
calificacion_2 = float(input("ingrese la calificacion 2:\n"))
calificacion_3 = float(input("ingrese la calificacion 3:\n"))

#proceso
promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

#salida
print(" el promedio de las e calificaciones es =", promedio)