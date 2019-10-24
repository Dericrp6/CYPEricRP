SERIE = 0
N = int(input("dame un entero positivo: "))

for i in range(1,10,N):
    SERIE = SERIE + i**i
    i = i + 1 
else: 
    print("no puedo calcular esos resultados")
