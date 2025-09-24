# AC 2nd What Is My Grade

grade = float(input("What is your grade percentage without percentage sign: "))

if grade >= 94:
    print("You have an A")
elif grade >= 90:
    print("You have an A-")
elif grade >= 87:
    print("You have an B+")
elif grade >= 84:
    print("You have an B")
elif grade >= 80:
    print("You have an B-")
elif grade >= 77:
    print("You have an C+")
elif grade >= 74:
    print("You have an C")
elif grade >= 70:
    print("You have an C-")
elif grade >= 67:
    print("You have an D+")
elif grade >= 64:
    print("You have an D")
elif grade >= 60:
    print("You have an D-")
else:
    print("You have an F")