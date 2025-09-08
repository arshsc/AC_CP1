# AC 2nd Basic Calculator

num_one = float(input("Enter the first number: "))
num_two = float(input("Enter the second number: "))

addition = num_one + num_two
subtraction = num_one - num_two
multiplication = num_one / num_two
division = num_one / num_two
int_division = num_one // num_two
modulo = num_one % num_two
exponent = num_one ** num_two

print(f"{num_one} + {num_two} = {addition:.2f}")
print(f"{num_one} - {num_two} = {subtraction:.2f}")
print(f"{num_one} * {num_two} = {multiplication:.2f}")
print(f"{num_one} / {num_two} = {division:.2f}")
print(f"{num_one} // {num_two} = {int_division:.2f}")
print(f"{num_one} % {num_two} = {modulo:.2f}")
print(f"{num_one} ^ {num_two} = {exponent:.2f}")