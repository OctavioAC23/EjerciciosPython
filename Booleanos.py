cadena1 = "Intento de texto"
print(cadena1.isupper())
print(cadena1.startswith("I"))
print(cadena1.endswith("o"))

letra = input("Ingresa una letra: ")

if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print ("Es una vocal")
else:
    print("No es vocal")

numero = int(input("Ingresa un numero: "))

if numero > 0:
    print("El valor absoluto: "+str(numero))
elif numero < 0:
    print("El valor absoluto: "+str(numero*-1))