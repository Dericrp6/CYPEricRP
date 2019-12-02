#Ps 2.11

#Construya un diagrama de flujo tal que dado como dato Y,
#calcule el resultado de la sig función

print("Construya un diagrama de flujo tal que dado como dato Y,")
print("calcule el resultado de la siguiente funcion")
Y = int(input("Dame un numero para calcular las siguientes funciones: "))

if 0 < Y and Y <= 11:
    F1 = ((3)== (Y) + (36))
    print (f"El calculo de la funcion es {F1}")
else:
    print("Este numero no es aceptable")

if 11 < Y and Y <= 33:
    F1 = ((Y**2) - (10))
    print(f"El calculo de la funcion {Y}^2 - 10 es: {F1} ")


if 33 < Y and Y <= 64:

    print("Este numero no es aceptable")

if 11 < Y and Y <= 33:
    F1 = ((Y**2) - (10))
    print(f"El calculo de la funcion {Y}^2 - 10 es: {F1} ")

    F1 = ((Y**3) + (Y**2) - (1))
    print(f"El calculo de la función {Y}^3 + {Y}^2 -1 es: {F1}")
else :
    print("Ese número no es aceptable")

if Y >64:
    F1 = 0
    print(f"El calculo de la función 0 es igual a {F1}")
