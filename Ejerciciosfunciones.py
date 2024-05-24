lista = []
listaPar = []
listaImpar = []
def agregar():
    numero = int(input("Ingrese un numero a la Lista = "))
    lista.append(numero)

def ParoImpar():
    if lista[len(lista)-1] % 2 == 0:
        listaPar.append(lista[len(lista)-1])
    else:
        listaImpar.append(lista[len(lista)-1])
    

i = 1
while i != 2:
    agregar()
    print(lista)
    ParoImpar()
    print("La lista Par "+str(listaPar))
    print("La lista Impar "+str(listaImpar))

    