# AC 2nd Maze Generator

import turtle
import random

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

rowturt = turtle.Turtle()
rowturt.penup()
rowturt.teleport(0, 0)

colturt = turtle.Turtle()
colturt.penup()
colturt.teleport(0, 0)
colturt.left(90)

count = 0

def turtley(ycord, turtletype):
    turtletype.teleport(0, ycord)
    ycord += 10

def turtlex(xcord, turtletype):
    turtletype.teleport(xcord, 0)
    xcord += 10

for rows in maze_rows:
    turtley(0, rowturt)
    for i in rows:
        if i == 0:
            count += 1
            rowturt.penup()
            rowturt.forward(10)
        elif i == 1:
            count += 1  
            rowturt.pendown()
            rowturt.forward(10)
    
for cols in maze_cols:
    turtlex(0, colturt)    
    for i in cols:
        if i == 0:
            count += 1
            colturt.penup()
            colturt.forward(10)
        elif i == 1:
            count += 1  
            colturt.pendown()
            colturt.forward(10)  

turtle.done()