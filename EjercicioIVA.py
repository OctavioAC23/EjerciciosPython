def ConPorcentaje(SinIVA,Porcentaje):
    Por = Porcentaje *.01
    return SinIVA * Por

def SinPorcentaje (SinIVA):
    return SinIVA*.21

SinIVA = float(input("Ingresa la cantidad sin IVA = "))
Porcentaje = int(input("Porcentaje del IVA = "))

if Porcentaje != 0:
    print(ConPorcentaje(SinIVA,Porcentaje))
else:
    print(SinPorcentaje(SinIVA))