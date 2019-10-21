NOM = 0 
SUE = float(input("Cual es su sueldo?: "))

for SUE in range(SUE < 1001 > -1):
    if SUE < 1000:
        NSUE = SUE*1.15

    else:
        NSUE = SUE*1.12

    NOM = NOM+NSUE
    print(f"Su nuevo sueldo es de {NSUE}")

    print(f"Su sueldo anterior {SUE}")

else:
    print(f"Esta es su nomina {NOM}")



