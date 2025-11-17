# AC 2nd Flexible Calculator

# Import needed libraries
import statistics

# Welcome the user to the calculator
print("Welcome to the Flexible Calculator!")

# Tell the user the available operations

# A function to take the numbers the user gives and uses the operation picked on them.

def operation(*numbers, operation):
    print("\nEnter numbers (Type 'done' when finished):")
    print("\nAvailable operations: sum, average, max, min, product")
    while True:
        for num in numbers:
            input(f"\nNumber: {num}")
            if num.isdigit():
                for i in num:
                    
            elif num == "Done":
                print()
            else:
                print("Invalid Number, please try again.")

operation_input = input("\nWhich operation would you like to perform? ")
operation("num1", "num2", operation=operation_input)