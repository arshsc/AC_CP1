# AC 2nd Turtle Race

# Import the libraries
import turtle
import random

# Create the Finish Line
turtle.hideturtle()
turtle.pensize(10)
turtle.teleport(500, -300)
turtle.speed(100)
turtle.left(90)
turtle.forward(600)

# Spawn in the turtles
red = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()
green = turtle.Turtle()
purple = turtle.Turtle()

# Function to setup the turtles
def turtlesetup(name, turtlecolor, teleportx, teleporty):
    name.color(turtlecolor)
    name.teleport(teleportx, teleporty)
    name.shape("turtle")
    name.turtlesize(1.5)

# Calling the function for each color
turtlesetup(red, "red" ,-500, 200)
turtlesetup(blue, "blue", -500, 100)
turtlesetup(yellow, "yellow", -500, 0)
turtlesetup(green, "green", -500, -100)
turtlesetup(purple, "purple", -500, -200)

steps = random.randint(10, 200)

while True:
    for i in range(1,10):
        steps = random.randint(10, 200)
        red.forward(steps)
        steps = random.randint(10, 200)
        blue.forward(steps)
        steps = random.randint(10, 200)
        yellow.forward(steps)
        steps = random.randint(10, 200)
        green.forward(steps)
        steps = random.randint(10, 200)
        purple.forward(steps)
        break
    

turtle.done()

# first turtle for pos to get across finish line declared winner
