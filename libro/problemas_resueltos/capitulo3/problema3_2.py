BAND = T
SUMSER = 0
I = 2

for I in range(I <= 1800):
    SUMSER = SUMSER + 1 
    print(f"la serie sera {I}")

    if BAND == T:
        BAND = F
        I = 1+3

    else:
        SERIE = SERIE-1/I
        BAND = T
        I = 1+2

print(f"Los terminos de la serie son {SUMSER}")

