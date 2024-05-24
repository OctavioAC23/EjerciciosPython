def Comparar():
    Primer = int(input("Primer numero a comparar = "))
    segundo = int(input("Segundo numero a comparar = "))
    if(Primer < segundo):
        return -1
    elif Primer > segundo:
        return 1
    elif Primer == segundo:
        return 0

print(Comparar())
