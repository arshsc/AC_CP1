# AC 2nd Password Strength

# Step 1: Ask user for their password initalize strength score 0, and set all requirements to false
password = input("Enter your password: ")

score = 0

length_req = False
uppercase_req = False
lowercase_req = False
number_req = False
special_char_req = False

# Step 2: Check the factors
while True:
    # Atleast 8 Character Length
    if len(password) >= 8:
         length_req = True
         score += 1
         continue
    # Atleast 1 Uppercase letter
    check_upper = any(char.isupper() for char in password)
    print(check_upper)
    # Atleast 1 Lowercase letter
    # Atleast 1 Number
    # Atleast 1 Special Character

# Step 3: Calculate the strength
# Length Requirement: +1 point
# Containing uppercase letter: +1 point
# Containing lowercase letter: +1 point
# Containing a number: +1 point
# Containing a special character: +1 point

# Step 4: Give a strength score
# Add the points up and print with corresponding level of strength
# Tell the user what their missing in the password