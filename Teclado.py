import math
variableA = int(input('Variable A: '))
variableB = int(input('Variable B: '))
variableC = int(input('Variable C: '))

Raiz = math.sqrt(pow(variableB,2)-4*(variableA*variableC))

X1 = (-variableB + Raiz)/(2*variableA)

X2 = (-variableB - Raiz)/(2*variableA)


print("La solucion es X1 = "+str(X1)+"\nX2 = "+str(X2))
