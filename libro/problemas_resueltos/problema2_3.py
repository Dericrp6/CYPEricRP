print("ECUACION_SEGUNDO_GRADO")

A = float(input("Dame un numero: "))
B = float(input("Dame otro numero:  "))
C = float(input("Dame otro numero: "))

DIS = B ** 2 - 4 * A * C

if DIS >= 0:
    X1 = ((-B)+DIS**0.5)/2*A
    X2 = ((-B)-DIS**0.5)/2*A
    print(f"Las raices reales despues de su ecuacion de segundo grado son {X1} {X2}")

else:
    print("No puedo calcular esa expresion")



