CHI = 0
MED = 0
GRA = 0
N = float(input("Dame el numero de ventas del vendedor: "))

I = 1
for I in range(1,I,N):
    V = int(input("Su numero de ventas porfavor: "))
    if V <= 200:
        CHI = CHIC + 1
        
    elif V < 400:
        MED = MED + 1 
    else: GRA = GRA + 1 

    I = I + 1

print(f"Las ventas menores fueron {CHI}")
print(f"Las ventas medianas fueron {MED}")
print(f"Las ventas mayores fueron {GRA}")


