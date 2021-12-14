import turtle
import time
import random

# Creating window

win = turtle.Screen()
win.title("Race")

# Register shapes
win.register_shape("cerbb.gif")
win.register_shape("monked.gif")
win.register_shape("spungebub.gif")
win.register_shape("winnie.gif")

turtle.bgcolor("light green")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-145, 195)
fontcolor = turtle.color("Brown")
turtle.write("GRAND RACE", font=("MathJax_Typewriter", 45, "bold"))
turtle.penup()

# Finish Line
stamp_size = 30
square_size = 15  # declaring variables
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()

# kavid
kavid = turtle.Turtle()
kavid.speed(0)
kavid.color("black")
kavid.shape("monked.gif")
kavid.penup()
kavid.goto(-250, 125)
turtle.pendown()

# cerby
crebby = turtle.Turtle()
crebby.speed(0)
crebby.color("red")
crebby.shape("cerbb.gif")
crebby.penup()
crebby.goto(-250, 65)
turtle.pendown()

# spongebob
sponge = turtle.Turtle()
sponge.speed(0)
sponge.color("purple")
sponge.shape("spungebub.gif")
sponge.penup()
sponge.goto(-250, -30)
turtle.pendown()

# winnie
winnie = turtle.Turtle()
winnie.speed(0)
winnie.color("yellow")
winnie.shape("winnie.gif")
winnie.penup()
winnie.goto(-250, -110)
turtle.pendown()

# Declaring names
fontcolor = turtle.color("brown")
# kavid
turtle.penup()
turtle.goto(-395, 115)
turtle.write("Kavid", font=("MathJax_Typewriter", 15, "bold"))
turtle.pendown()

# crebby
turtle.penup()
turtle.goto(-395, 55)
turtle.write("Crebby", font=("MathJax_Typewriter", 15, "bold"))
turtle.pendown()

# spongebob
turtle.penup()
turtle.goto(-395, -40)
turtle.write("Spongebob", font=("MathJax_Typewriter", 15, "bold"))
turtle.pendown()

# winnie
turtle.penup()
turtle.goto(-395, -120)
turtle.write("Winnie", font=("MathJax_Typewriter", 15, "bold"))
turtle.pendown()

time.sleep(1)

# Start the race
while kavid.xcor() <= 180 and crebby.xcor() <= 180 and sponge.xcor() <= 180 and winnie.xcor() <= 180:
    kavid.forward(random.randint(1, 5))
    crebby.forward(random.randint(1, 5))
    sponge.forward(random.randint(1, 5))
    winnie.forward(random.randint(1, 5))

turtle.penup()

# Declaring the Winner
if kavid.xcor() > crebby.xcor() and kavid.xcor() > sponge.xcor() and kavid.xcor() > winnie.xcor():
    print("Kavid won the race")
    turtle.setpos(-165, -195)
    fontcolor = turtle.color("Brown")
    turtle.write("Kavid is the Winner", font=("MathJax_Typewriter", 30, "bold"))


elif crebby.xcor() > kavid.xcor() and crebby.xcor() > sponge.xcor() and crebby.xcor() > winnie.xcor():
    print("Crebby is the winner")
    turtle.setpos(-185, -195)
    fontcolor = turtle.color("Brown")
    turtle.write("Creeby is the winner", font=("MathJax_Typewriter", 30, "bold"))


elif sponge.xcor() > kavid.xcor() and sponge.xcor() > crebby.xcor() and sponge.xcor() > winnie.xcor():
    print("Spongebob is the winner")
    turtle.setpos(-215, -195)
    fontcolor = turtle.color("Brown")
    turtle.write("SpongeBob is the winner", font=("MathJax_Typewriter", 30, "bold"))


else:
    print("Winnie is the winner")
    turtle.setpos(-175, -195)
    fontcolor = turtle.color("Brown")
    turtle.write("Winnie is the winner", font=("MathJax_Typewriter", 30, "bold"))

turtle.done()
