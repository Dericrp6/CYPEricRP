SERIE = 0 
N = float(input("Dame un numero entero: "))
T = 0
F = 0
BAND = T
I = 1

for I in (1,N):
    if BAND == T:
        SERIE + 1/I
        BAND == F

    else:
        SERIE = SERIE -1/I
        BAND == T

    I = I + 1

else:
    print(f"Su serie es {SERIE}")
    
