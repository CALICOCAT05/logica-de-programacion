#. Hacer una función para que imprima un arreglo o lista de 10 elementos numéricos insertados uno por uno y ordenados de forma ascendente y mostrarlos en pantalla

num1 = int(input("ingrese el primer numero de la lista "))
num2 = int(input("ingrese el segundo numero de la lista "))
num3 = int(input("ingrese el tercer numero de la lista "))
num4 = int(input("ingrese el cuarto numero de la lista "))
num5 = int(input("ingrese el quinto numero de la lista "))
num6 = int(input("ingrese el sexto numero de la lista "))
num7 = int(input("ingrese el septimo numero de la lista "))
num8 = int(input("ingrese el octavo numero de la lista "))
num9 = int(input("ingrese el noveno numero de la lista "))
num10 = int(input("ingrese el decimo numero de la lista "))

lista_numeros = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]

print("lista en el orden ingresado:")
print(lista_numeros)

print("lista ordenada de forma ascendente:")
lista_numeros.sort()
print(lista_numeros)
