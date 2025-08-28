# AC 2nd Average Grade

first_period = float(input("What is your 1st period class grade? "))
second_period = float(input("What is your 2nd period class grade? "))
third_period = float(input("What is your 3rd period class grade? "))
fourth_period = float(input("What is your 4th period class grade? "))
fifth_period = float(input("What is your 5th period class grade? "))
sixth_period = float(input("What is your 6th period class grade? "))
seventh_period = float(input("What is your 7th period class grade? "))

grade_average = ((first_period + second_period + third_period + fourth_period + fifth_period + sixth_period +seventh_period)/7)
print(round(grade_average, 2), "is your grade average.")