class Fabrica():
    def __init__(self,llantas,color,precio):
        self.llantas = llantas
        self.color=color
        self.precio=precio

class Moto(Fabrica):
    def datos(self):
        print("La cantidad de llantas la moto es de: ",self.llantas)
        print("El color de la moto es: ",self.color)
        print("El Precio de la moto es de: $",self.precio)

class Carro(Fabrica):
    def datos(self):
        print("La cantidad de llantas del carro es de: ",self.llantas)
        print("El color del carro es: ",self.color)
        print("El Precio del carro es de: $",self.precio)

moto = Moto(2,"Negro",20000)
moto.datos()

carro = Carro(4,"Blanco",45000)
carro.datos()