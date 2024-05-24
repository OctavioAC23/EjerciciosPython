import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("red") #ca,bia el color de fondo
s.title("Proyecto de Personalizacion")
t.shapesize(10,5,1) #ancho,largo y profundizar

t.fillcolor("orange")#cambia el color del apuntador
t.forward(100)

t.pencolor("white")#color del borde
t.forward(100)

t.color("green","blue")
t.right(90)
t.forward(100)

t.pensize(5) #se hace mas grueso la linea
t.forward(100)
turtle.done()