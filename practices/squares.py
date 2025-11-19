# AC 2nd Squared Numbers

numbers = [3,7,12,25,30,45,50,65,70,85,90,105,110,125,130,145,150,165,170,185] # Defining the list with the all the numbers in it
squared = list(map(lambda num: num**2, numbers)) # Using map and lambda to square each number and then turn it into a list
for i, num in enumerate(numbers): # Print each num in numbers and then the squared of each number
    print(f"Original: {num}, Squared: {squared[i]}")