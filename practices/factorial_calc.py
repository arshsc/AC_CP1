# AC 2nd Factorial Calc


# Original Lizzie pseudocode:

# Function: It will take in a number and get every number that occures before it (num-1) and multiply it together

# def n!(num):
    # num_list = []
    # while num >= 1:
        # num_list.append(num)
    # for loop to multiply numbers in list


# Me making the pseudocode:

def n_factorial(num): #"n!" is not a valid function name, change to n_factorial
    num_list = []
    num_list.append(num) # append the original number before modifying it
    while num >= 1:
        num -= 1 # subtract -1 from the number
        num_list.append(num)
    factor = 1 # factoring
    for n in num_list:
        factor *= n # multiply all numbers to the factor variable
    return factor

number = int(input("Enter a number: ")) # the input
factored_number = n_factorial(number) # returning the factored number from the funciton
print(f"Original number: {number}\nFactored Number: {factored_number}") # printing the original and factored number