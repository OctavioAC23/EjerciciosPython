class Estudiante():
    def __init__(self,nombre,nota): #Se inicializa los atributos
        self.nombre = nombre #atributo que recibira el nombre 
        self.nota = nota #atributo que recibira la nota
    
    def Imprimir(self): #aqui hereda los atributos y mostrara el nombre y nota
        print("Nombre: {} \nNota: {}".format(self.nombre,self.nota))

    def resultados(self): #aqui evalua lo que heredo de la clase en pocas palabras lo que haya llegando a la clase
        if self.nota < 6 :
            print("Has Reprobado")
        else: 
            print("Has Aprobado")

nombre = input("Ingresa el nombre del Estudiante = ")
nota = int(input("Ingresa la calificacion de la nota = "))
estudiante = Estudiante(nombre,nota)
estudiante.Imprimir()
estudiante.resultados()
