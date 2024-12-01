#Realizar un programa que realice un cuestionario con las siguientes 12 preguntas, muestre su resultado aciertos / 12 y mostrar el calificación = (aciertos / 12) * 10:

# Lista de preguntas y sus respuestas correctas
preguntas = [
    ("Herramienta de programación, parecido al lenguaje español utilizado para crear código: \na) IDE     b) Pseudocódigo     c) Compilador     d) ANSI / ISO \nIngresa el inciso en minúsculas: ", "b"),
    ("Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.\na) Información     b) Datos     c) Programa     d) Código\nIngresa el inciso en minúsculas: ", "a"),
    ("Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo:\na) IEEE     b) IDE     c) ANSI/ISO     d) VSCode\nIngresa el inciso en minúsculas: ", "c"),
    ("Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema:\na) Proceso     b) Solución     c) Función     d) Algoritmo\nIngresa el inciso en minúsculas: ", "d"),
    ("Conjunto de elementos que se relacionan para cumplir una función determinada:\na) Estructura     b) Datos     c) Operación     d) Sistema\nIngresa el inciso en minúsculas: ", "d"),
    ("Componente de un IDE que se encarga de traducir el código fuente a código máquina:\na) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete\nIngresa el inciso en minúsculas: ", "d"),
    ("Elemento que se usa para almacenar una cantidad donde cambia su valor:\na) Constante     b) Variable     c) Librería     d) Tipo de Dato\nIngresa el inciso en minúsculas: ", "b"),
    ("Conjunto de símbolos, letras, números que no tienen un significado:\na) Datos     b) Estructura     c) Información     d) Sistema\nIngresa el inciso en minúsculas: ", "a"),
    ("Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento:\na) Filosofía     b) Sociología     c) Lógica     d) Argumentación\nIngresa el inciso en minúsculas: ", "c"),
    ("Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto:\na) Evento     b) Estándar     c) Calidad     d) Productividad\nIngresa el inciso en minúsculas: ", "b"),
    ("Conjunto de elementos ordenados que componen y son la base de algo físico o no físico:\na) Estructura     b) Sistema     c) Objeto     d) Virtual\nIngresa el inciso en minúsculas: ", "a"),
    ("Conjunto de instrucciones (código) que indican a la computadora tareas a realizar:\na) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando\nIngresa el inciso en minúsculas: ", "c"),
]

aciertos = 0

for pregunta, respuesta_correcta in preguntas:
    respuesta_usuario = input(pregunta)
    if respuesta_usuario == respuesta_correcta:
        aciertos += 1  


print("Aciertos:",aciertos / len (preguntas))
calificacion = (aciertos / len(preguntas)) * 10 
print("Calificación final:", calificacion)


