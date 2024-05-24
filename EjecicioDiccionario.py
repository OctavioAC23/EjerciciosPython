diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
Pais = input("Ingresa un Pais = ")
letra = Pais.capitalize() in diccionario #busca en el diccionario

if letra== True:
    print("La capital es "+diccionario[Pais])
else:
    print("No existe carnal")

jugadores = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}

numero = int(input("Ingresa el numero de tu jugardor = "))
Verificar = numero.conjugate() in jugadores
if Verificar == True:
    print(jugadores[numero])
else:
    print("no hay carnal")