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
turtles = ["red"]
red = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()
green = turtle.Turtle()
purple = turtle.Turtle()

# Function to setup the turtles
def turtlesetup(name, turtle_color, teleport_x, teleport_y):
    name.color(turtle_color)
    name.teleport(teleport_x, teleport_y)
    name.shape("turtle")
    name.turtlesize(1.5)

# Calling the function for each color
turtlesetup(red, "red" ,-500, 200)
turtlesetup(blue, "blue", -500, 100)
turtlesetup(yellow, "yellow", -500, 0)
turtlesetup(green, "green", -500, -100)
turtlesetup(purple, "purple", -500, -200)

# Setup function for win condition

turtle_finish = turtle.Turtle()

def turtle_win(name, turtle_color):
        turtle_finish.hideturtle()
        turtle_finish.color(turtle_color)
        turtle_finish.penup()
        turtle_finish.teleport(0, 350)
        turtle_finish.pendown()
        turtle_finish.write(f"{turtle_color} Wins!", move=False, align="center", font=("Arial", 40, "normal"))
        turtle_finish.penup()
    
game_running = True
while game_running == True:
    for i in range(10):
        steps = random.randint(10, 100)
        red.forward(steps)
        if round(red.xcor(), 1) >= 500:
            turtle_win("Red")
            game_running = False
            break

        steps = random.randint(10, 100)
        blue.forward(steps)
        if round(blue.xcor(), 1) >= 500:
            turtle_win(blue, "Blue")
            game_running = False
            break

        steps = random.randint(10, 100)
        yellow.forward(steps)
        if round(yellow.xcor(), 1) >= 500:
            turtle_win(yellow, "Yellow")
            game_running = False
            break

        steps = random.randint(10, 100)
        green.forward(steps)
        if round(green.xcor(), 1) >= 500:
            turtle_win(green, "Green")
            game_running = False
            break

        steps = random.randint(10, 100)
        purple.forward(steps)
        if round(purple.xcor(), 1) >= 500:
            turtle_win(purple, "Purple")
            game_running = False
            break
    break

turtle.done()
