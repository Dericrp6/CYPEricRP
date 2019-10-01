print("AUMENTO_SELECTIVA_SIMPLE")
SUE = int(input("Cual es su sueldo?: $"))

if SUE < 1000: 
    AUM = SUE * 0.15
    NSUE = SUE + AUM
    print("Puede ser acredor del aumento")
    print(f"Tu nuevo sueldo es de ${NSUE}")

else:
    print("No puedes ser acredor del aumento")
    
