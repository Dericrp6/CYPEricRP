N = int(input("ingrese el numero de elementos del arreglo: "))
VEC = []
if N >= 1 and N< 500:
    #logica
    for i in range(0,N,1):
        VEC.append(int(input("ingresa valor: ")))
    VEC.sort()
    print("Lista de numeros sin repeticiones: ")
    i = 0
    while i <= N-1:
        print(VEC[i])
        REPET = VEC[i]
        while i <= N-1 and REPET == VEC[i]:
            i += 1

else:
    print("el numero de elemento de arreglos es incorrecto")
