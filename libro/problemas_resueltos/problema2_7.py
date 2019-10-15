print("ORDEN_CRECIENTE")

A = int(input("Introduce un entero positivo: "))
B = int(input("Introduce otro valor entero positivo: "))
C = int(input("Introduce otro valor entero positivo: "))

if A < B:
    if B < C:
        print(f"Los numeros {A},{B},{C} estan en orden creciente")
    else: 
        print(f"Los numeros {A},{B},{C} no estan en orden creciente")

else: 
    print(f"Los numeros {A},{B},{C} no estan en orden creciente")
    

