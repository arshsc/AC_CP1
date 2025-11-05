# AC 2nd Maze Generator

# Import needed libraries
import turtle
import random

# Set the two variables, a list with multiple nested lists inside representing each row or column
maze_rows = [[random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]]

maze_cols = [[random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]]

# Set the turtles for row and column
#turtle.Turtle()
#turtle.pensize(5)
#turtle.forward(300)
#turtle.left(90)
#turtle.forward(300)
#turtle.left(90)
#turtle.forward(300)
#turtle.left(90)
#turtle.forward(300)
#turtle.left(90)

rowturt = turtle.Turtle()
rowturt.speed(5)
rowturt.hideturtle()
rowturt.pensize(5)
rowturt.penup()
rowturt.teleport(0, 0)

colturt = turtle.Turtle()
colturt.speed(5)
colturt.hideturtle()
colturt.pensize(5)
colturt.penup()
colturt.teleport(0, 0)
colturt.left(90)


# Function to check if the maze is solvable
def is_solvable(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()
        if x == size - 1 and y == size - 1:
            return True
        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and col_grid[y][x + 1] == 0:
            stack.append((x + 1, y))
        if y < size - 1 and row_grid[y + 1][x] == 0:
            stack.append((x, y + 1))
        if x > 0 and col_grid[y][x] == 0:
            stack.append((x - 1, y))
        if y > 0 and row_grid[y][x] == 0:
            stack.append((x, y - 1))
    return False

def turtley(ycord, turtletype):
        turtletype.teleport(0, ycord)
        ycord += 50

def turtlex(xcord, turtletype):
        turtletype.teleport(xcord, 0)
        xcord += 50

def drawmaze(group, turttype):
    for row in group:
        for grid in row:
            if grid == 0:
                turttype.penup()
                turttype.forward(50)
            if grid == 1:
                turttype.pendown()
                turttype.forward(50)
        turttype.teleport(0, 50)



drawmaze(maze_rows, rowturt)
#drawmaze(maze_cols, colturt)


turtle.done()