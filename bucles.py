#while
i = 0

while i < 10:
    i+=1
    print("Toy chambiando {}".format(i))

#for
lista = ['Uno','Dos','Tres']

for i in lista:
    print(i)

#range
for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

#breakContinue

for i in range(1,11):
    if i == 2:
        continue #omite un dato pero sigue adelante
    if i == 5:
        break #termina aqui
    print(i)