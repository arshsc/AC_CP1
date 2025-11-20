# AC 2nd Flexible Calculator


# Libraries
import statistics


# Functions
# Function to ask the user what operation they want to pick
def operation_choice():
    operations = ["sum", "average", "max", "min", "product"]

    print("\nAvailable operations: sum, average, max, min, product")
    
    while True:
        choice = input("\nWhich operation would you like to perform? ").lower()
        if choice in operations:
            return choice
        else:
            print("\nInvalid operation, please try again.")

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

# Function to calculate the chosen operation on the list
def operation(num_list, operation):
    if not num_list:
        print("\nNo numbers were entered, cannot perform the operation.")
        return
    
    numbers_string = ", ".join(map(str, num_list))

    if operation == "sum":
        total_sum = sum(num_list)
        print(f"\nCalculating {operation} of: {numbers_string}\nResult: {total_sum}")
    elif operation == "average":
        average = statistics.mean(num_list)
        print(f"\nCalculating {operation} of: {numbers_string}\nResult: {average}")
    elif operation == "max":
        max_num = max(num_list)
        print(f"\nCalculating {operation} of: {numbers_string}\nResult: {max_num}")
    elif operation == "min":
        min_num = min(num_list)
        print(f"\nCalculating {operation} of: {numbers_string}\nResult: {min_num}")
    elif operation == "product":
        product = 1
        for num in num_list:
            product *= num
        print(f"\nCalculating {operation} of: {numbers_string}\nResult: {product}")
    else:
        print("\nThis shouldn't be possible!")


# Welcome the user to the calculator
print("Welcome to the Flexible Calculator!")

# Put the calculator in a loop to keep it running unless exited
while True:
    # The number list, also resets it to blank if another calculation needs to be performed
    numbers_list = []

    # Calling the functions
    operation_chosen = operation_choice()
    number_inputs(num_list=numbers_list)
    operation(numbers_list, operation_chosen)

    # Ask the user if they want to perform another calculation and use conditionals to respond
    again = input("\nWould you like to perform another calculation? (yes/no) ").strip().lower()
    if again in ("yes", "y"):
        continue
    elif again in ("no", "n"):
        print("\nThank you for using the Flexible Calculator!")
        break