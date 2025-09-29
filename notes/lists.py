# AC 2nd List Notes

import random

names = ["Alex", "Katie", "Cora", "Andrew", "Jake", "Eric", 5, 3.14, False]

print(names)
print(names[5])
print(names[random.randint(1, len(names))])
print(random.choice(names))
names[-1] = "Xavier"
names.extend(["Treyson", "Tia"])
names += ["Joseph", "Israel", "Zee"]
names.remove(3.14)
x = names.index("Jake")
names.insert(3, "Vienna")
names.pop(x)
print(names)

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]

board[1][1] = "X"

print(board)
# List (changable, ordered)
# Tuple (Not changeable, ordered)
classes = ("Bard", "Monk", "Barbarian", "Paladin")

# Set (changable, unordered)
fruit = {"Apple", "Orange", "Strawberry", "Kiwi"}
print(fruit)