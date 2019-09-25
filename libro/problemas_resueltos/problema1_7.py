print("AREA_TRIANGULO")

L1 = float(input("Dame el lado 1: "))
L2 = float(input("Dame el lado 2: "))
L3 = float(input("Dame el lado 3: "))

S = (L1 + L2 + L3)/2
AREA = (S *(S - L1) * (S - L2) * (S - L3)) **0.5

print(f"El area del triangulo es {AREA}")

