#Pedir el nivel del agua en metros de una cisterna

#varibales
metros = 0

#entrada
metros = float(input("ingresa en metros el nivel de agua que hay dentro de la cisterna:\n"))

#salida
if(metros > 6):
    print("desbordamiento de agua en cisterna")
elif(metros == 6):
    print("apagar bomba")
elif(metros >= 5 and metros <= 6 ):
    print("desacelerar la bomba")
elif(metros >= 3 and metros <= 4):
    print("Bomba trabajando")
elif(metros > 0 and metros <= 2):
    print("acelerar bomba de agua")
elif(metros == 0):
    print("encender bomba de agua")
elif(metros < 0):
    print("fuga en cisterna")