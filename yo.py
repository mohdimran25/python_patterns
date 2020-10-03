import turtle
wn=turtle.Screen()
wn.bgcolor("light blue")
wn.title("yoyoyo")
pen= turtle.Turtle()
pen.pendown()
pen.pencolor("red")
pen.fillcolor("green")
pen.shape("turtle")
def sqrfunc(size):
    for side in range(4):
        pen.fd(size)
        pen.left(90)
        size+=5
sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
sqrfunc(6)

turtle.done()
