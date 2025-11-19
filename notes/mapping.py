# AC 2nd Mapping Notes

numbers = [6468, 35765, 38536, 3676, 65, 86754, 74367, 83636]
"""divided = []

for num in numbers:
    divided.append(num/2)"""

"""def divide(number):
    return number/2"""

divided = map(lambda num: num/2, numbers)

print(divided)

"""for i, num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}")"""