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
def number_inputs(*number, num_list):
    print("\nEnter whole numbers (Type 'done' when finished):")
    while True:
        number = input("Number: ").strip()
        if number.lower() == "done":
            break
        elif number.isnumeric() == True:
            int_number = int(number)
            num_list.append(int_number)
            continue
        else:
            print("Not a number, please try again.")
            continue

def operation(num_list, operation):
    if operation == "sum":
        total_sum = sum(num_list)
        print(f"Calculating {operation} of: {num_list}\nResult: {total_sum}")

# Welcome the user to the calculator
print("Welcome to the Flexible Calculator!")


operation_chosen = operation_choice()
number_inputs(num_list=numbers_list)
print(numbers_list)
operation(numbers_list, operation_chosen)