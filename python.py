import turtle

t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)

colors = ['blue', 'red', 'purple', 'green', 'purple', 'orange']

for i in range(150):
  t.pencolor(colors[i % 6])
  t.circle(190 - i / 2, 90)
  t.left(90)
  t.circle(190 - i / 3, 90)
  t.left(60)

turtle.done()
