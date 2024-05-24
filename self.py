#class FabricaTelefonos():
#    marca = "Samsung"
    
#    def ElaborarHuawei(self):
#        self.marca = "Huawei"

#telefono = FabricaTelefonos()
#telefono.ElaborarHuawei() 
#print(telefono.marca)

class FabricaTelefonos():    
    def __init__(self,marca,color):
            self.marca = marca
            self.color = color
    #def __str__(self): el objeto es
    #def __del__(self): el objeto es destruido 
telefono = FabricaTelefonos('Huawei', 'Negro')
print(telefono.marca)