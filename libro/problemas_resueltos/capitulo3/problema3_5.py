SUMOTR = 0
SUMPOS = 0
CUEPOS = 0

N = float(input("Dame un numero entero: "))
I = 1

for I in range(I <= N):
    NUM = float(input("Dame otro numero: "))
    if NUM > 0:
        SUMPOS = SUMPOS + NUM 
        CUEPOS = CUEPOS + 1

    else:
        SUMOTR = SUMOTR + NUM

    I = I + 1

else:
    PROGEN = (SUMPOS + SUMOTR)/N
    PROPOS = (SUMPOS/CUEPOS)

print(f"El total de numeros positivos son {CUEPOS}")
print(f"El promedio de los numeros positivos es {PROPOS}")
print(f"El promedio general de los numeros positivos es de {PROGEN}")

