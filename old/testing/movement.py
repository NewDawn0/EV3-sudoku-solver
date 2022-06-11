
import turtle

# ===> Constants & Global Variables
# <Variable description>
turtle.color('black')
turtle.hideturtle()
turtle.pensize = 5
turtle.speed(0)

# ===> Functions & Classes
# <Function description>
def penup():
    turtle.penup()

def pendown():
    turtle.pendown()

def pos():
    return turtle.position()

def done():
    turtle.done()

def goto(x, y):
    turtle.goto(pos() + (x, y))


def dot(rad):
    turtle.dot(rad, "black")
