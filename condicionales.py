#mayoria de edad
from decimal import Decimal, ROUND_HALF_UP

edad = int(input("escribe tu edad: "))
edad = edad.quantize(Decimal("0.0"), rounding=ROUND_HALF_UP)
print(edad)

if (edad >= 18 and edad <= 120): #rango valido 18 hasta 120
    print("mayor de edad")
elif (edad >= 0 and edad <= 17): #rango valido 0 a 17
    print("menor de edad")
elif(edad < 0 or edad > 120): #valores no valifos menor que 0 o mayor que 120
    print("edad no valida")
else:
    print("otra cosa")