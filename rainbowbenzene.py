import turtle
colors=['red','purple','blue','green','orange','yellow']
t=turtle.Pen()
turtle.speed(900000000000000)
turtle.bgcolor('black')
for i in range(360):
    t.pencolor(colors[i%6])
    t.width(i/100+1)
    t.forward(i)
    t.left(59)
exitonclick()