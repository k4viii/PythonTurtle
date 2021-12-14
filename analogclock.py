import time
import turtle

win = turtle.Screen()
win.bgcolor("black")
win.setup(width=800)
win.title("Analog Clock")
win.tracer(0)

# pn = pen
pn = turtle.Turtle()
pn.hideturtle()
pn.speed(0)
pn.pensize(3)


def draw_clock(hr, m, sec, pn):  # pen is argument for clock

    # clock outline
    pn.up()
    pn.goto(0, 210)
    pn.setheading(180)
    pn.color("green")
    pn.pendown()
    pn.circle(210)

    pn.penup()
    pn.home()
    pn.goto(0, -247)
    pn.pendown()
    pn.circle(250)

    # hours lines
    pn.penup()
    pn.goto(0, 0)
    pn.setheading(90)

    for i in range(12):
        pn.forward(190)
        pn.pendown()
        pn.forward(20)
        pn.penup()
        pn.goto(0, 0)
        pn.right(30)

    # hour hand
    pn.penup()
    pn.goto(0, 0)
    pn.color("blue")
    pn.setheading(90)
    angle = (hr / 12) * 360
    pn.right(angle)
    pn.pendown()
    pn.forward(60)

    # minute hand
    pn.penup()
    pn.goto(0, 0)
    pn.color("red")
    pn.setheading(90)
    angle = (m / 60) * 360
    pn.right(angle)
    pn.pendown()
    pn.forward(120)

    # second hand
    pn.penup()
    pn.goto(0, 0)
    pn.color("yellow")
    pn.setheading(90)
    angle = (sec / 60) * 360
    pn.right(angle)
    pn.pendown()
    pn.forward(155)


# updating time
while True:
    hr = int(time.strftime("%I"))  # hour
    m = int(time.strftime("%M"))  # minutes
    sec = int(time.strftime("%s"))  # second

    draw_clock(hr, m, sec, pn)
    win.update()

    time.sleep(1)

    pn.clear()  # avoid overlapping
