# print tiene 4 formas de uso
"""
1.- con comas
2.- con signo'+'
3.- con la funciòn format()
4.- Es con una variable de format()
"""
# con comas , concatenar agregando
# un espacio y haciendo un casting de tipo 
edad = 10
nombre = "Eric"
estatura = 1.67
print(edad , estatura , nombre)
# con '+' hace lo mismo pero no
# realiza el casting automàtico
# no agrega espacio 
print( str(edad) + str(estatura) + nombre)

# 3.- funcion format()

print("Nombre: {} Edad: {} ".format(nombre, edad,))

# 4.- con una variable de format() simplificada

print(f"Nombre: \"{nombre}\" \nEdad:\t{edad} ")

# print y el argunmento end

print("solo hay 10 tipos de personas, las que saben binario y las que no",end="\n")
print("otra linea")
