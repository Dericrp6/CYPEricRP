otra = bool(int(input("Hay mas alumnos? (0 No, 1 Si):")))
suma = 0.0
cont=0

while(otra == True):  #4<5
    cal = float(input("calificacion: "))
    cont += 1
    suma += cal 
    otra = bool(int(input("Hay mas alumnos? (0 No, 1 Si):")))

print("Suma", suma)
print("promedio:", suma/cont)
print("Fin del programa")

