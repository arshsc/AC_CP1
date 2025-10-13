# AC 2nd Password Strength

# Step 1: Ask user for their password initalize strength score 0, and set all requirements to false
password = input("Enter your password: ")

score = 0

length_req = False
uppercase_req = False
lowercase_req = False
number_req = False
special_char_req = False

# Define Special Characters
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ".", ",", ":", ";", "<", ">", "?", "[", "]", "{", "}", "|"]

# Step 2: Check the factors, if any requirements meet set the boolean to true
    # Atleast 8 Character Length
if len(password) >= 8:
    length_req = True
    score += 1
    # Atleast 1 Uppercase letter
if any(char.isupper() for char in password):
    uppercase_req = True
    score += 1
    # Atleast 1 Lowercase letter
if any(char.islower() for char in password):
    lowercase_req = True
    score += 1
    # Atleast 1 Number
if any(char.isdigit() for char in password):
    number_req = True
    score += 1
    # Atleast 1 Special Character
for item in special_characters:
    if item in password:
        special_char_req = True
        score += 1
        break

# Step 3: Calculate the strength
# Length Requirement: +1 point
# Containing uppercase letter: +1 point
# Containing lowercase letter: +1 point
# Containing a number: +1 point
# Containing a special character: +1 point

# Display Password Strength Assessment
print(f"\nPassword Strength Assessment:\nLength (8+ Characters): {length_req}\nContains Uppercase: {uppercase_req}\nContains Lowercase: {lowercase_req}\nContains a Number: {number_req}\nContains a Special Character: {special_char_req}\n")

# Step 4: Give a strength score
# Add the points up and print with corresponding level of strength
if score == 1 or score == 2:
    print(f"Strength Score: {score}/5\nPassword Strength: Weak")
elif score == 3:
    print(f"Strength Score: {score}/5\nPassword Strength: Moderate")
elif score == 4:
    print(f"Strength Score: {score}/5\nPassword Strength: Strong")
elif score == 5:
    print(f"Strength Score: {score}/5\nPassword Strength: Very Strong")
else:
    print("This shouldn't be possible")