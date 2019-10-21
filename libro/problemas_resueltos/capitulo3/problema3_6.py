MAY = -100000
MEN = 100000
N = int(input("Dame un numero: "))

I = 1

for I in range(1,14,N):
    NUM = int(input("Dame otro numero: "))
    if NUM > MAY:
        MAY = NUM

    if NUM < MEN:
        MEN = NUM
    I = I + 1 

print(f"El valor mayor es {MAY}")
print(f"El valor menor es de {MEN}")

