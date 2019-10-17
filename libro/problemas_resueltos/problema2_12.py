SUE = int(input("Cual es su sueldo?: "))
CATE = int(input("Cual es su categoria como trabajador?: "))
HE = int(input("Cuantas horas extras trabajo?: "))

if CATE:
    PHE = 0

elif HE > 30:
    NSUE = SUE + 30*PHE

else:
    NSUE = SUE + HE*PHE

print(f"Su nuevo sueldo es de {NSUE}")

