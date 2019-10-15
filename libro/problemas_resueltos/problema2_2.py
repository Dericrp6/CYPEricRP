print("EXPRESION")

P = int(input("Dame un numero entero: "))
Q = int(input("Dame otro numero entero: "))

EXP = P ** 3 + Q ** 4 - 2 * P ** 2

if EXP < 680:
    print(f"Las operaciones expresadas son {P} y {Q} ")

else:
    print("No puedo calcular ese valor")

print("Fin del programa")

