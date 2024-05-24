import turtle



'''t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
'''
'''for i in range(4):
    t.forward(100)
    t.right(90)'''
resultado = input("¿Quieres imprimir una figura? ")
if resultado == "si":
    s = turtle.Screen()
    t = turtle.Turtle()
    for i in range(10,100,10):
        t.circle(i)
    turtle.done()
else:
    print("Sacate de aqui")