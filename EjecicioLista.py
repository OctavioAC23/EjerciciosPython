lista = [20,50,"Curso",'Python',3.14]
print(lista)
PrimerDato = input("Ingresa el primer dato a sustituir: ")
lista.insert(0,PrimerDato)
SegundoDato = input("Ingresa el segundo dato a sustituir: ")
lista.insert(1,SegundoDato)
print(lista)

Numero = []
for i in range (1,11):
    Numero.append(i)

print(Numero)
Numero[3] = Numero[3]*2
Numero[6] = Numero[6]*2
Numero[8] = Numero[8]*2
print(Numero)
