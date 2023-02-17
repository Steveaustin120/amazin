import turtle as t
import colorsys

t.bgcolor("blue")
t.speed("fastest")
t.tracer(100)
t.pencolor("green")
hue = 0.7
t.hideturtle()

def func():
    global hue
    for i in range(3):
        color = colorsys.hue_to_rgb(hue,1,1)
        hue += 0.001
        t.fillcolor(color)
        t.begin_fill()
        t.fd(100)
        t.right(20)
        t.fd(100)
        t.lt(20)
        t.end_fill()
for j in range(400):
    func()
    t.goto(8,8)
    t.rt(188)
    .exitonclick()