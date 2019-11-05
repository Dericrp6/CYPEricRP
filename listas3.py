autos = ["akura","mazda","honda","toyota","nissan"]
motos = ["ducati","kawasaki","harley davidson","bmw","italika"]
bicis = ["benotto","bmx","apache","mercurio","trek"]
vehiculos = [autos,motos,bicis]

print(motos[2])
print(vehiculos[1][2])
print(vehiculos[2][4])
print(autos[1:4:1])
print(motos[-2:-5:-1])
print(bicis[-1::-1]) #[::-1] es los mismo

print(vehiculos[2][1:4:1])
print(vehiculos[1::])
