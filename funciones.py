'''
def nombre_de_la funcion(parametros o argumentos)
    contenido de la funcion
'''
#entrada y proceso de datos
def operacion_sumar(num1, num2): #la funcion recibe/obtiene 2 parametros o argumentos
    #contenido de la funcion
    return num1 + num2          #retorna, regresa o devuelve un valor(es)

def operacion_resta(num1, num2): #la funcion recibe/obtiene 2 parametros o argumentos
    #contenido de la funcion
    resta = num1 - num2          #retorna, regresa o devuelve un valor(es)
    print(resta)

def operacion_multiplicacion(num1, num2):
    #contenido de la funcion
    multiplicacion = num1 * num2
    print(multiplicacion)

def operacion_division(num1,num2):
    #contenido de la funcion
    division = num1 / num2
    print(division)

#salida de datos
"invocar o mandar a llamar la funcion"
fn1 = operacion_sumar(10,15.5) #se le pasan o envian 2 parametros a la funcion
fn2 = operacion_sumar("dana", "paola")
operacion_resta(20, 15)
operacion_multiplicacion(8,7)
operacion_division(100, 2)
print(fn1)
print(fn2)
