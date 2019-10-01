print("AUMENTO_SELECTIVA_DOBLE")

SUE = int(input("Cual es tu sueldo?: "))

if SUE <1000:
    NSUE = SUE * 1.15
    print("Eres acredor de un aumento del 15%")
    print(f"Su nuevo sueldo es de ${NSUE}")

else:
    NSUE = SUE * 1.12
    print("Eres acredor de un aumento del 12%")
    print(f"Su nuevo sueldo es de ${NSUE}")
