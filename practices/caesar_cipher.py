# AC 2nd Caesar Cipher

def encode(message, shift):
    for letter in message:
        if letter.isalpha():
            print(chr(ord(letter) + shift), end="")
        else:
            print(letter, end="")
    print()

def decode(message, shift):
    for letter in message:
        if letter.isalpha():
            print(chr(ord(letter) - shift), end="")
        else:
            print(letter, end="")
    print()

choice = input("Choose operatoin:\n(1) Encode\n(2) Decode\n")
message = input("Enter the message:\n")
shift_value = int(input("Enter a shift value as an integer:\n"))

#Encode
if choice == "1":
    encode(message, shift_value)
#Decode
elif choice == "2":
    decode(message, shift_value)
else:
    print("Invalid Option")