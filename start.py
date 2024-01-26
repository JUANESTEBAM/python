import turtle

# Configuración inicial
turtle.speed(2)
turtle.pensize(2)
turtle.color("orange")

# Cabeza de Goku
turtle.circle(100)

# Ojos
turtle.penup()
turtle.goto(-40, 120)
turtle.pendown()
turtle.dot(20)
turtle.penup()
turtle.goto(40, 120)
turtle.pendown()
turtle.dot(20)

# Boca
turtle.penup()
turtle.goto(-20, 80)
turtle.pendown()
turtle.right(90)
turtle.circle(20, 180)

# Cuerpo
turtle.penup()
turtle.goto(-50, 20)
turtle.pendown()
turtle.forward(100)
turtle.backward(200)
turtle.forward(100)

# Brazos
turtle.penup()
turtle.goto(-50, 20)
turtle.pendown()
turtle.left(45)
turtle.forward(80)
turtle.backward(80)
turtle.right(90)
turtle.forward(80)
turtle.backward(80)

# Piernas
turtle.penup()
turtle.goto(-50, -80)
turtle.pendown()
turtle.left(45)
turtle.forward(80)
turtle.backward(80)
turtle.right(90)
turtle.forward(80)
turtle.backward(80)

# Cerrar la ventana al hacer clic
turtle.exitonclick()
