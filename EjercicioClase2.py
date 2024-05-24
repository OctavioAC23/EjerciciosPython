class Calculadora():
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def suma(self):
        print(self.valor1 + self.valor2)
    def resta(self):
        print(self.valor1 - self.valor2)
    def multiplicacion(self):
        print(self.valor1 * self.valor2)
    def division(self):
        print(self.valor1/self.valor2)

valor1 = int(input("Ingresa valor 1 = "))
valor2 = int(input("Ingresa valor 2 = "))
valores = Calculadora(valor1,valor2)
valores.suma()
valores.resta()
valores.multiplicacion()
valores.division()
