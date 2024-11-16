# Pedir la cantidad de grados y convertirlos a °C, °F y K.

#variables
celsius = 0


#entrada
celsius =int(input("ingresa la temperatura en grados celsius\n"))

#procesos

c_a_f = (9*celsius/5)+32
c_a_k = celsius + 273.15
f_a_c = (5*(c_a_f-32))/9
f_a_k = (5*(c_a_f)-32)/9+32
k_a_c = c_a_k - 273.15
k_a_f = (9*(c_a_k-273.15))/5+32

#salida
print("la temperatura en grados celcius es:",celsius)
print("la temperatura en grados de celcius a fahrenheit es:",c_a_f)
print("la temperatura en grados de celcius a kelvin es:",c_a_k)
print("la temperatura en grados de fahrenheit a celcius es", f_a_c)
print("la temperatura en grados de fahnrenheit a kelvin es",f_a_k)
print("la temperatura en grados de kelvin a celcius es", k_a_c)
print("la temperatura en grados de kelvin a fahnrenheit es", k_a_f)