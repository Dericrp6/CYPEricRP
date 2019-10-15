print("PROMEDIO_ALUMNO")
MAT = int(input("Dame tu matricula: "))
CAL1 = float(input("Dame tu calificacion num. 1: "))
CAL2 = float(input("Dame tu calificacion num. 2: "))
CAL3 = float(input("Dame tu calificacion num. 3: "))
CAL4 = float(input("Dame tu calificacion num. 4: "))
CAL5 = float(input("Dame tu calificacion num. 5: "))

PRO = (CAL1+CAL2+CAL3+CAL4+CAL5)/5

if PRO >= 6:
    print(f"Tu numero de matricula {MAT} con un promedio de {PRO} es APROBATORIO")

else:
    print(f"Tu numero de matricula {MAT} con un promedio de {PRO} es REPROBATORIO")

