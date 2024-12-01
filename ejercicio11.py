#Pedir números enteros en un ciclo mientras sean positivos y en caso de que un número sea negativo cerrar el ciclo y al final promediar los

numeros = []

while True:
        numero = int(input("Ingresa un número entero positivo (o un número negativo para salir): "))
        if numero < 0:
            break 
        numeros.append(numero)


if numeros:  # Verificar que la lista no esté vacía
    promedio = sum(numeros) / len(numeros)
    print(f"Promedio de los números positivos ingresados: {promedio:.2f}")
else:
    print("No ingresaste ningún número positivo.")
