# AC 2nd Turtle Race

import turtle
import random


# Finish Line
turtle.hideturtle()
turtle.pensize(10)
turtle.teleport(500, -300)
turtle.speed(100)
turtle.left(90)
turtle.forward(600)

red = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()
green = turtle.Turtle()
purple = turtle.Turtle()

red.teleport(-500, 200)
red.forward(100)

blue.teleport(-500, 100)
blue.forward(100)

yellow.teleport(-500, 0)
yellow.forward(100)

green.teleport(-500, -100)
green.forward(100)

purple.teleport(-500, -200)
purple.forward(100)

turtle.done()


# spawn 5 different colored turtles and randomly generate speed
# first turtle for pos to get across finish line declared winner