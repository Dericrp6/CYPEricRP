print("TIENDA_DESCUENTOS")

NUM = float(input("Dame un numero entero positivo: "))
COMPRA = float(input("De cuanto fue su compra?: "))

if COMPRA < 500:
    PAGAR = COMPRA
    print(f"Usted tiene que pagar {PAGAR}")

elif COMPRA <= 1000:
    PAGAR = COMPRA - (COMPRA * 0.05)
    print(f"Usted debe pagar {PAGAR}")

elif COMPRA  <=7000:
    PAGAR = COMPRA - (COMPRA * 0.11)
    print(f"Usted debe pagar {PAGAR}")

elif COMPRA <=15000:
    PAGAR = COMPRA - (COMPRA * 0.18)
    print(f"Ustede debe pagar {PAGAR}")
else:
    PAGAR = COMPRA - (COMPRA * 0.25)
    print(f"Usted debe pagar {PAGAR}")



