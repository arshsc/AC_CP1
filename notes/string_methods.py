#AC 2nd String Methods

# .lower() => makes it all lowercase
# .upper() => makes it all uppercase
# .capitalize() => capitalizes the first letter
# .title() => capitalizes the first letter of every word

age = int(input("Bro how old are you?"))
name = input("What is your name").strip().title()
print("Hello {}, it is nice to meet you! You are {:.2f} years old!".format(name, age))
print(f"Hello {name}, it is nice to meet you! You are {age:.1f} years old!")

#age = input("Bro how old are you?")
#print(age isdigit())
#print("Really? " + age + "is old.")

sentence = "The quick brown fox jumps over the lazy dog!"
word = "brown"
print(sentence.find(word))
length = len(word)
print(sentence.replace(word, "yellow"))