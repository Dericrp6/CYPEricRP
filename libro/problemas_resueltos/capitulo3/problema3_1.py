SUMPAR = 0
SUMIMP = 0
CUEPAR = 0

I = 1

for I in (1,275):
    if I<= 270:

        NUM = int(input("dame un numero entero:"))
    
    elif (NUM >= 0):
        if (-1**NUM)>0:
            SUMPAR = SUMPAR + NUM
            CUEPAR = CUEPAR + 1 
        else:
            SUMIMP = SUMIMP + NUM

        I = 1 + 1 

else: 
    PROBAR = SUMPAR/CUEPAR
    print(f"{PROPAR} Y {SUMIMP}")
