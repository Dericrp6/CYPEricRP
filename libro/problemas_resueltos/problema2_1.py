print("GRILLO_TEMPERATURA")

N = int(input("Grillidos por minuto?: "))

if N > 0:
    T = N / 4 + 40
    print(f"La temeperatura dado los grillidos por minuto es de {T}")

else: 
    print("No existe tal temepratura")

print("Fin del programa")
