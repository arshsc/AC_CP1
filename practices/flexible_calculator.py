# AC 2nd Flexible Calculator

# Import needed libraries
import statistics

# Variables
# List to hold the numbers
numbers_list = []


# Functions
# Function to ask the user what operator they want to pick
def operation_choice():
    print("\nAvailable operations: sum, average, max, min, product")
    return input("\nWhich operation would you like to perform? ")

# Function to take in the numbers and add them into a list
def number_inputs(*numbers, num_list):
    print("\nEnter numbers (Type 'done' when finished):")
    while True:
        numbers = input("Number: ").strip().lower()
        if numbers == "done":
            break
        elif numbers.isdigit() == True:
            num_list.append(numbers)
            continue
        else:
            print("Not a number, please try again.")
            continue

"""def operation(*numbers, operation):
    print("\nAvailable operations: sum, average, max, min, product")"""

# Welcome the user to the calculator
print("Welcome to the Flexible Calculator!")


operation = operation_choice()

number_inputs(num_list=numbers_list)
print(numbers_list)