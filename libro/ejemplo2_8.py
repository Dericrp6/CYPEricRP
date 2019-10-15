CATE = int(input("En que categoria estas como trabajador del (1-4)?: "))
SUE = float(input("Cual es tu sueldo?: "))
NSUE = 0

if CATE == 1:
    NSUE = SUE * 1.15

if CATE == 2:
    NSUE = SUE * 1.10

if CATE == 3:
    NSUE = SUE * 1.08

if CATE == 4:
    NSUE = SUE * 1.07

print(NSUE)

print("Fin del programa")
