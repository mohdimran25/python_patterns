import turtle
wn=turtle.Screen()
turtle.speed(80)
for i in range(600):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()