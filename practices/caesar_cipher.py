# AC 2nd Caesar Cipher

# Use ASCII
print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")

choice = input("Choose operaton:\n(1) Encode\n(2) Decode\n")
message = input("Enter the message:\n")
shift_value = input("Enter a shift value as an integer:\n")

#Encode
if choice == "1":
    for letter in message:
#Decode
if choice == "2":
    for letter in message: