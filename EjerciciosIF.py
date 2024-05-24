palabra1 = input("Ingresa una palabra ")
palabra2 = input("Ingresa otra palabra ")

if palabra1[-3: ] == palabra2[-3: ]:
    print("Riman un poco")
else:
    print("No riman")

Opcion = input("Seleccione a su candidato\nCandidato A por el partido rojo\nCandidato B por el partido verde\nCandidato C por el partido azul\n=")
if Opcion.upper() == 'A':
    print("Usted ha votado por el partido rojo")
elif Opcion.upper() == 'B':
    print("Usted ha votado por el partido verde")
elif Opcion.upper() == 'C':
    print("Usted ha votado por el partido azul")
else:
    print("Opcion erronea")