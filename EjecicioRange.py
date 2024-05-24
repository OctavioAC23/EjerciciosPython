for i in range(1,11):
    print(i)

Inicio = int(input("Ingresa el numero para iniciar el rango "))
Final = int(input("Ingresa el numero para terminar el rango"))

for i in range(Inicio,Final+1):
    print(i)
    
for i in range(Inicio,Final+1):
    if i % 2 == 0:
        continue 
    print(i)