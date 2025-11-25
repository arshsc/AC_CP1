# AC 2nd Factorial Calc


# Lizzies original pseudocode:

# Function: It will take in a number and get every number that occures before it (num-1) and multiply it together

# def n!(num):
    # num_list = []
    # while num >= 1:
        # num_list.append(num)
    # for loop to multiply numbers in list


# me using the pseudocode + additions to make it work and follow the rubric:

def n_factorial(num): #"n!" is not a valid function name, change to n_factorial
    num_list = []
    num_list.append(num) # append the original number before modifying it
    if num == 0: # the factor of 0 is 1
        return 1, [0]
    while num > 1: # stops before 0
        num -= 1 # subtract -1 from the number
        num_list.append(num)
    factor = 1 # factoring
    for n in num_list:
        factor *= n # multiply all numbers to the factor variable
    return factor, num_list # returning the factored number


while True: # whole code in a loop so it keeps asking
    valid_num = False # variable to store if the number is valid
    while valid_num == False: # loop to keep asking to get a valid num
        number = input("\nWhat number do you want the factorial of: ") # input to ask for the number
        if not number.isdigit(): # checks to see if number is not a digit
            print("\nInvalid input, please enter a whole number") # tells the user to retyr
            continue # continues the loop
        number = int(number) # changes the number input to an int
        if number < 0: # checks to see if number is less than 0
            print("\nInvalid input, please enter a whole number") # retrys as you cannot do a negative factorial
        else: # if the number is valid
            valid_num = True # makes the variable true

    factored_number, num_list = n_factorial(number) # returning the factored number from the funciton

    multiplying = "" # blank variable
    for n in num_list: # getting each number in the number list
        multiplying += str(n) + " x " # puts an x inbetween each number
    multiplying = multiplying[:-3] # gets rid of the last x as there is no need for it

    print(f"{multiplying} = {factored_number}") # printing the original and factored number