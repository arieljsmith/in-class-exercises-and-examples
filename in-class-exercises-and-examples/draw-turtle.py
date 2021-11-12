# Instructions for this exercise are here https://realpython.com/beginners-guide-python-turtle/
abyss = input("Gaze into the abyss? (Type yes or no): ")
if abyss == "yes":
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

    # movement
    # t.right(90)
    # t.forward(100)
    # t.left(90)
    # t.backward(100)

    # alt movement (using x,y coords)
    # t.goto(100, 0)
    # t.goto(100, -100)
    # t.goto(0, -100)
    # t.home()

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

    # diamond
    # t.pensize(6)
    t.penup()
    t.goto(-71, 0)
    t.pendown()
    t.goto(0, 71)
    t.goto(71, 0)
    t.goto(0, -71)
    t.goto(-71, 0)
    # t.goto(125, -50)

    # circle
    # t.pensize(4)
    t.penup()
    t.goto(0, -71)
    t.pendown()
    t.circle(71.5)

    # smaller circle
    # t.pensize(7)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.circle(50)

    t.penup()
    t.goto(0, -100)
    t.pendown()

    # while loop circles
    n = 100
    p = 3
    while n <= 150:
        t.pensize(p)
        t.circle(n)
        n = n + 25
        p = p - 1
        t.penup()
        t.goto(0, -n)
        t.pendown()

    t.penup()
    t.goto(0, 113)
    t.pendown()

    # for loop triangles, top only
    x = 0
    y = 113
    p = 1
    for i in range(7):
        t.pensize(p)
        t.goto((x + 57), (y+100))
        t.goto((x - 57), (y+100))
        t.goto(x, y)
        y = y + 51
        p = p + 1
        t.penup()
        t.goto(x, y)
        t.pendown()

    t.penup()
    t.goto(0, -503)
    t.pendown()

    # for loop circles, bottom only
    p = 7
    c = 145
    x = 0
    y = -503
    for j in range(7):
        t.pensize(p)
        t.circle(c)
        y = y - 176
        c = c + 100
        p = p - 1
        t.penup()
        t.goto(x, y)
        t.pendown()

    # turtle leaves the arena
    t.penup()
    t.goto(0, -500)
    t.pendown()

    # keeps the window open
    turtle.mainloop()

else:
    print("Suit yourself.")
