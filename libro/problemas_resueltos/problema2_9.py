print("IMPUESTO_ARTICULO")

PREBAS = float(input("Cual es el precio basico del producto??: "))

if PREBAS > 500:
    IMP = 20 * 0.30+ (PREBAS-40)*0.50
    PRETOT = PREBAS + IMP #
    
elif PREBAS > 40:
     IMP = 20 * 0.30+ (PREBAS-40)*0.40

elif PREBAS > 20:
     IMP = 20 * 0.30+ (PREBAS-20)*0.30



PRETOT = PREBAS + IMP

print(f"El precio de su producto {PREBAS} tendra un impuesto de {IMP}")
print(f"El precio total del producto es de {PRETOT}")

