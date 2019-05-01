import turtle
def flower(turtle):
    turtle.color("red","yellow")
    turtle.begin_fill()

    for i in range(50):
        turtle.forward(300)
        turtle.left(170)

        turtle.end_fill()
        #turtle.done()
#import turtle
import math
import random
def sqrt(turtle):
    bob = turtle.Turtle()
    turtle.colormode(255)
    bob.speed(10)

    for i in range(2000):
        bob.forward(math.sqrt(i))
        bob.left(i%180)
#import turtle
#import math
#import random
def siunsoid(turtle):
    bob = turtle.Turtle()
    turtle.colormode(255)
    bob.speed(10)

    for i in range(2000):
    	bob.forward(10)
    	bob.left(math.sin(i/10)*25)
    	bob.left(20)

    turtle.done()
    print ("flower")
def simple(turtle):
    keith = turtle.Turtle()

    keith.speed(1)

    keith.forward(100)
    keith.left(45)
    keith.forward(100)

    #turtle.done()

def shape(turtle):
    bob = turtle.Turtle()

    bob.color("blue", "cyan")

    # Square
    bob.begin_fill()
    bob.forward(100)
    bob.setheading(90)
    bob.forward(100)
    bob.setheading(180)
    bob.forward(100)
    bob.setheading(270)
    bob.forward(100)
    bob.end_fill()

    bob.penup()
    bob.setheading(270)
    bob.forward(120)
    bob.pendown()

    bob.begin_fill()
    bob.setheading(0)
    bob.forward(100)
    bob.setheading(90)
    bob.forward(100)
    bob.setheading(180)
    bob.forward(100)
    bob.setheading(270)
    bob.forward(100)
    bob.end_fill()


def pen_up_down(turtle):

    bob = turtle.Turtle()
    bob.getscreen().bgcolor("#994444")
    bob.penup()
    bob.goto((-200,100))
    bob.pendown()

def star(turtle, size):
	if size <= 10:
		return
	else:
		turtle.begin_fill()
		for i in range(5):
			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)
		turtle.end_fill()

# basic lines and turns
simple(turtle)

# simple shapes  & colour  & pen up & down
shape(turtle)

flower(turtle)

sinusoid(turtle)

pen_up_down(turtle)

star(turtle, 360)
turtle.done()
