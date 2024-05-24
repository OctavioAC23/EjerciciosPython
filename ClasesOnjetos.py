class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128
    
    def llamar(self,mensaje):
        return mensaje
    
    def escucharMusica(self):
        print("Estas escuchando Musica")
    
telefono = FabricaTelefonos() #tiene acceso a los demas atributos
telefono.marca
telefono.color
telefono.almacenamiento
telefono.memoriaRam

print(telefono.llamar("Hola, ¿Con quien hablo?"))
telefono.escucharMusica()