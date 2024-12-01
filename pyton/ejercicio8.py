#Calcular la nómina para un empleado en el mes de Mayo del 2023 conociendosu pago por día de $250.-

nomina = input("¿trabajaste todos los dias de mayo del 2023 o solo de lunes a viernes? (si o no) ")

if(nomina == "si"):
    nomina_total = 250 * 23 
    print("tranajaste 23 dias y tu nomina es de :", nomina_total)
elif(nomina == "no"):
    nomina_total2 = 250 * 31
    print("tranajaste 31 dias y el valor de tu nomina es", nomina_total2)
