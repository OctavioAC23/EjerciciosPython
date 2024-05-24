import turtle
import random

s = turtle.Screen()
s.title("Primer Proyecto")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

jugador1.shape("turtle")
jugador1.color("green","green")

jugador2.shape("turtle")
jugador2.color("red","red")

jugador1.penup() #oculta el apuntador
jugador1.goto(200,50)
jugador1.pendown()
jugador1.circle(40)
jugador1.penup()
jugador1.goto(160,90)
jugador1.right(180)
jugador1.pendown()
jugador1.forward(250)
jugador1.right(180)

jugador2.penup() #oculta el apuntador
jugador2.goto(200,-50)
jugador2.pendown()
jugador2.circle(40)
jugador2.penup()
jugador2.goto(160,-10)
jugador2.right(180)
jugador2.pendown()
jugador2.forward(250)
jugador2.right(180)

dado = [1,2,3,4,5,6]


for i in range(20):
    if jugador1.pos() >=(200,50):
        print("Jugador 1 ha ganado")
        break
    elif jugador2.pos() >=(200,-50):
        print("Jugador 2 ha ganado")
        break
    else:
        turno1 = input("Presiona la tecla enter para avanzar.")
        turno1 = random.choice(dado)
        jugador1.forward(10*turno1)
        turno2 = random.choice(dado)
        jugador2.forward(10*turno2)

t = turtle.done()
