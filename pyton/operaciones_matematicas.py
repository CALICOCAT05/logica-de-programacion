#operaciones matematicas: suma, resta, mult, div, potencia, raiz cuadrada, raiz cubica, modulo

#importar las librerias o bibliotecas que contienen funciones
import math

#declarar o crear constantes
dato_1 = 0 #valor inicial
dato_2 = 0 #valor inicial

#entrada
dato_1 = float(input("ingrese un numero"))
dato_2 = float(input("ingrese un numero"))


#proceso (se realizan las operaciones y caclulos matematicos y/o logicos)
suma = dato_1 + dato_2 #suma
resta = dato_1 - dato_2 #resta
multiplicacion = dato_1 * dato_2 #multiplicacion
division = dato_1 / dato_2 #division

potencia_1 = dato_1 ** dato_2 #potencia
potencia_2 = pow(dato_1, dato_2) #las funciones tienen  parantesis donde se colocan parametros o argumentos
cuadrado = dato_1 ** 2
cubo = pow(dato_2, 3)

raiz_cuadrada_1 = math.sqrt(16)
raiz_cuadrada_2 = pow(16, 1/2)
raiz_cubica = pow(27, 1/3)

modulo_residuo_1 = 10 % 2
modulo_residuo_2 = dato_1 % dato_2


#salida
print("la suma es igual = ", suma) #concatenacion con ,
print ("la resta es igual = " + str (resta) ) #concatenacion con + por casteo
print (f"la multiplicacion es igual = {multiplicacion}") #interpolacion de texto
print ("la divison es igual =", division)
print ("la potencia de N1 elevada a N2 =", potencia_1)
print ("la potencia de n1 elevado a n2 =", potencia_2)
print ("el cuadrado de n1 es =", cuadrado)
print ("el cubo de n2 es =", cubo)
print ("la raiz cuadrada de 16 es=", raiz_cuadrada_1)
print ("la raiz cuadrada de 16 es ", raiz_cuadrada_2)
print ("la raiz cubica de 27 es=", raiz_cubica)
print ("el modulo 1 o residuo es=", modulo_residuo_1)
print ("el modulo 2 o residuo es=", modulo_residuo_2)