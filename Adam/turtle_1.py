import turtle

tortoise = turtle.Turtle()


def square():
    for i in range(4):
        tortoise.pencolor('red')
        tortoise.forward(50)
        tortoise.right(90)


def stopsign():
    for i in range(8):
        tortoise.pencolor('blue')
        tortoise.right(45)
        tortoise.forward(100)


def rombusz():
    tortoise.pencolor('light green')
    tortoise.pensize(2)
    tortoise.right(60)
    for i in range(2):
        tortoise.forward(100)
        tortoise.left(120)
        tortoise.forward(100)
        tortoise.left(60)


def circle():
    tortoise.pencolor('dark blue')
    tortoise.pensize(2)
    for i in range(360):
        tortoise.forward(3)
        tortoise.right(10)


circle()
turtle.done()
