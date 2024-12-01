#Crear una lista o arreglo de diccionarios de 5 estados de México con los datos de nombre, población, extensión

estados_mexico = [
    {"nombre": "Chihuahua", "poblacion": 3935114, "extension": 247455},  # km²
    {"nombre": "Jalisco", "poblacion": 8348131, "extension": 78588},    # km²
    {"nombre": "Yucatán", "poblacion": 2361265, "extension": 39524},    # km²
    {"nombre": "Ciudad de México", "poblacion": 9209944, "extension": 1485},  # km²
    {"nombre": "Nuevo León", "poblacion": 5581473, "extension": 64156}   # km²
]

# Mostrar la información de los estados
for estado in estados_mexico:
    print(f"Estado: {estado['nombre']}, Población: {estado['poblacion']}, Extensión: {estado['extension']} km²")
