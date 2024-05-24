import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

s = turtle.Screen()
t = turtle.Turtle()

s.setup(550,550)
s.title("Juego de Snake")
s.bgcolor("black")

Serpiente = turtle.Turtle()
Serpiente.speed(1)
Serpiente.shape("square")
Serpiente.color("green","green")
Serpiente.penup()
Serpiente.goto(0,0)
Serpiente.direction = 'stop'

comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)

cuerpo = []
texto = turtle.Turtle()
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,-200)
texto.write("Marcador: 0\t Marcador mas alto: 0",align="center",font=("normal",20,"normal"))
def arriba():
    Serpiente.direction = 'up'
def abajo():
    Serpiente.direction = 'down'
def derecha():
    Serpiente.direction = 'right'
def izquierda():
    Serpiente.direction = 'left'

def movimiento():
    if Serpiente.direction == 'up':
        y = Serpiente.ycor()
        Serpiente.sety(y + 20)
    elif Serpiente.direction == 'down':
        y = Serpiente.ycor()
        Serpiente.sety(y - 20)
    elif Serpiente.direction == 'right':
        x = Serpiente.xcor()
        Serpiente.setx(x + 20)
    elif Serpiente.direction == 'left':
        x = Serpiente.xcor()
        Serpiente.setx(x - 20)
        
s.listen()
# Asignar las teclas a las funciones correspondientes
s.onkeypress(arriba, "w")
s.onkeypress(abajo, "s")
s.onkeypress(derecha, "d")
s.onkeypress(izquierda, "a")
while True:
    s.update()
    if Serpiente.xcor() > 250 or Serpiente.xcor() < -250 or Serpiente.ycor() > 250 or Serpiente.ycor() < -250:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        Serpiente.home()
        Serpiente.direction = 'stop'
        cuerpo.clear()
        marcador = 0
        texto.clear()
        texto.write("Marcador: {}\tMarcador mas alto:{}".format(marcador,marcador_alto),align="center",font=("normal",20,"normal"))


    if Serpiente.distance(comida) < 20 :
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)
        
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador 
            texto.clear()
            texto.write("Marcador: {}\tMarcador mas alto:{}".format(marcador,marcador_alto),align="center",font=("normal",20,"normal"))
    
    total = len(cuerpo)
    for i in range(total - 1,0,-1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)
            
    if total > 0:
        x = Serpiente.xcor()
        y = Serpiente.ycor()
        cuerpo[0].goto(x,y)
        

    movimiento()
    
    for i in cuerpo:
        if i.distance(Serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            Serpiente.home()
            cuerpo.clear()
            Serpiente.direction = "stop"

    time.sleep(retraso)
    
turtle.done()