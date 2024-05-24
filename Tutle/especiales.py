import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10)
t.circle(10)
t.speed(10)
t.circle(50)
t.dot(30)

t.hideturtle() #oculta el apuntador
t.speed(1)
t.circle(40)
t.showturtle() #aparece el apuntador
t.circle(100)

t.setx(100) #mantiene el eje x
t.sety(-100) #mantiene el eje y

t.penup()#no dibuja nada
t.forward(100)

t.undo()#repite la ultima accion 
t.clear()#elimina lo ultimo que hizo 
t.forward(100)
t.stamp()

turtle.done()