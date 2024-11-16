#2. Calcular el área y perímetro de un círculo.

#declarar variables
pi = 3.1416
radio = 0

#entrada
radio = float(input("ingrese el valor del radio del circulo:\n"))

#procesos
perimetro = 2*(pi*radio) 
area = pi*(radio**2)

#salida
print("el perimeto del circulo es =", perimetro )
print("el area del circulo es =", area)
