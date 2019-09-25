PERA = int(input("Dame tu edad: "))
PERB = int(input("Dame tu edad: "))
PERC = int(input("Dame tu edad: "))

if PERA > PERB and PERA > PERC:
    print(f"{PERA} es la persona mas grand ")
if PERB > PERA and PERB > PERC:
    print(f"{PERB} es la persona mas grande")
if PERC > PERA and PERC > PERB:
    print(f"{PERC} es la persona mas grande")

print("Otra solucion")
if PERA != PERB and PERA != PERC and PERB != PERC:
    if PERA > PERB and PERA > PERC:
        print(PERA, "Es el mayor")
    else:
        if PERB > PERA and PERB > PERC:
            print(PERB, "Es el mayor")
        else:
            print(PERC, "Es el mayor")


