#Obtener valores para: a, b y c. Calcular la fórmula general.

#libreria
import math

#variables
a = 0
b = 0
c = 0

#entrada
a = float(input("ingresa el valor de a\n"))
b = float(input("ingresa el valor de b\n"))
c = float(input("ingresa el valor de c\n"))

#procesos
raiz = (b**2) - (4*a*c)
x1 = (-b -math.sqrt(raiz))/2*a
x2 = (-b +math.sqrt(raiz))/2*a

#salida
print(" el resulado de x1 mediante la formula general es", x1)
print ("el resultado de x2 mediante la formula general es",x2 )