#AC 2nd Idiot Proof

full_name = input("What is your full name: ").strip().title()
phone = input("What is your phone number: ").strip().replace("-", " ")
gpa = float(input("what is your GPA: ").strip())

print(f"Name: {full_name}\nPhone Number: {phone}\nGPA: {gpa:.1f}")