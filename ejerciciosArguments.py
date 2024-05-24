import math
def Circulo(radio):
    return pow(radio,2) * math.pi

def Area(b,a):
    return b*a

def tamanio(*lista):
    return(len(lista))

base = int(input("Ingresa la Base = "))
altura = int(input("Ingresa la Altura = "))
radio = int(input("Radio de un circulo = "))

print("Area del Rectangulo = "+str(Area(base,altura)))
print("Area del Circulo = "+str(Circulo(radio)))

print(tamanio(1,2,3,4,5,6,7,8,9,10))