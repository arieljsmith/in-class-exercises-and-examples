# Instructions for this exercise are here https://realpython.com/beginners-guide-python-turtle/

# basic setup
import turtle
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("#463745")
turtle.title("Ceci n'est pas une Turtle")
t.shapesize(1, 1, 1)
turtle.fillcolor("#463745")
turtle.pencolor("#463745")
t.fillcolor("#463745")
t.pencolor("#FFBB53")
t.shape("triangle")
t.pensize(1)
t.speed(15)

# square alt movement fill
t.pensize(4)
t.penup()
t.goto(-50, 50)
t.pendown()
t.begin_fill()
t.goto(50, 50)
t.goto(50, -50)
t.goto(-50, -50)
t.goto(-50, 50)
t.end_fill()

# keeps the window open
turtle.mainloop()
