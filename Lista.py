lista = ['Python',120,'Nombre',4.14]
print(lista)
print(len(lista))
lista[0] = "python"
print(lista[0:2])
print(lista[ :3])
print(lista[2: ])
print(lista[-1])
print(lista[-4:-1])

lista.append(543) #Agregar
print(lista)

lista.insert(2,'Prueba') #agregar en X lugar
print(lista)

print(lista.count(1)) #Buscar en la Lista
print(lista.index(4.14)) #Buscar en donde esta en la lista
lista.sort() #acomoda en orden
lista.reverse() #acomoda al revez

lista.pop() #elimina la ultima de la lista
lista.remove(120) #elimina un X elemento de la lista