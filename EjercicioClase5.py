#Crear un programa con tres clases Universidad, 
# con atributos nombre (Donde se almacena el nombre de la Universidad). 
#Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
#Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
#El programa debe imprimir la especialidad, edad,
# nombre y universidad de dicho estudiante con un objeto llamado persona.
class Universidad(): #este inicializa todo
    def __init__(self,Nombre):
        self.Nombre = Nombre

class Carrera(): #aqui solo almacena un nombre
    def Carrera(self,especialidad):
        self.especialidad = especialidad
 
class Estudiante(Universidad,Carrera): #primero hereda el anterior junto su inicializacion
    def Datos(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print("MI nombre es {}\n,tengo {} años\nmi especialidad es {}. Estudio en la Univerdad {}".format(self.nombre,self.edad,self.especialidad,self.Nombre))

persona = Estudiante("ESCOM") #primero se pide el primer dato para inicializar
persona.Carrera("Sistemas") #depsues se puede aplazar la informacion heredad
persona.Datos("Miguel Angel",23) #al final el def para los funciones