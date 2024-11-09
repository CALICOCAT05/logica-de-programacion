#operaciones matematicas: suma, resta, mult, div, potencia, raiz cuadrada, raiz cubica, modulo

#declarar o crear constantes
dato_1 = 0 #valor inicial
dato_2 = 0 #valor inicial

#entrada
dato_1 = int(input("ingrese un numero"))
dato_2 = int(input("ingrese un numero"))


#proceso (se realizan las operaciones y caclulos matematicos y/o logicos)
suma =dato_1 + dato_2 #suma
resta =dato_1 - dato_2 #resta
multiplicacion= dato_1 * dato_2 #multiplicacion
division =dato_1 / dato_2 #division

#salida
print("la suma es igual = ", suma) #concatenacion con ,
print ("la resta es igual = " + str (resta) ) #concatenacion con + por casteo
print (f"la multiplicacion es igual = {multiplicacion}") #interpolacion de texto
print ("la divison es igual =", division)