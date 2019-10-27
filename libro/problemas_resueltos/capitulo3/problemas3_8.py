NUM = int(input("Dame un numero entero:"))

if NUM > 0:
    for i in range(1,77,10):
        NUM = int(input("Dame otro numero: "))
    if (-1**NUM) > 0:
        NUM = NUM / 2

    else:
        NUM = NUM * 3 + 1
        print (f"sucesion {NUM}")

else:
    print(f"{NUM} tiene que ser un entero positivo")


