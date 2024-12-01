#ejercicio 9
import random
import string
import os

def mostrar_menu():
    print("********menu**********")
    print("(a)Mostrar una lista de 3 servicios de pasaje con sus estrellas de calificación")
    print("(b) Calcular la nómina de un empleado en ENERO del 2024")
    print("(c)Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error")
    print("(d)pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos")

def lista_medios_trasnporte():
    lista_pasajes = ["metro", "avion", "metrobus"]
    lista_estrellas_calificacion = [3,4,5]
    print(lista_pasajes, lista_estrellas_calificacion)

def calcular_nomina():
    if(nomina == "si"):
        nomina_total = 250 * 31 
        print("tranajaste 31 dias y tu nomina es de :", nomina_total)
    elif(nomina == "no"):
        nomina_total2 = 250 * 23
        print("tranajaste 23 dias (lunes a viernes) y el valor de tu nomina es", nomina_total2)



def generar_contraseña(numero_caracteres):
    if(numero_caracteres <= 5):
    # Definir los caracteres a utilizar
        caracteres = string.ascii_letters + string.digits + string.punctuation
    # Generar la contraseña aleatoria
        contraseña = ''.join(random.choice(caracteres) for _ in range(numero_caracteres))
        return contraseña
    elif(numero_caracteres > 5):
        return "error"


respuesta = "si"

while(respuesta == "si"):
    os.system('cls') # clear screen
    mostrar_menu() #invocar o mandar a llamar la funcion
    opcion = input("elige una opcion del menu: ")


    if(opcion == "a" or opcion == "A" or opcion == "(a)"):
        lista_medios_trasnporte()
    elif(opcion == "b" or opcion == "B" or opcion == "(b)"):
        nomina = input("¿trabajaste todos los dias de enero del 2024 o solo de lunes a viernes? (si o no) ")
        calcular_nomina()
    elif(opcion == "c" or opcion == "C" or opcion == "(c)"):
        caracteres = int(input("¿cuantos caracteres? "))
        generar_contraseña(caracteres)
    elif(opcion == "d" or opcion == "d" or opcion == "(d)"):
        primer_ap = input("¿cual es tu primer apellido? ")
        segundo_ap = input("cual es tu segundo apellido? ")
        edad = input ("¿cual es tu edad? ")
        print("hola",primer_ap,segundo_ap, "tienes", edad, "años")


    else:
        print("opcion no valida")
    
    respuesta = input("quieres continuar?: ")
