# AC 2nd Caesar Cipher

# Use ASCII
print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")

def encode(shift, message):

    
choice = input("Choose operaton:\n(1) Encode\n(2) Decode\n")
message = input("Enter the message:\n")
shift_value = input("Enter a shift value as an integer:\n")
