# AC 2nd Combat Program

import random

monster_health = 50
flee_chance = random.randint(1, 4)

def players_turn():
    players_choice = input("What would you like to do?\n(1) Normal Attack\n(2) Wild Attack (2x Damage but you will also take damage\n(3) Drink a healing potion (+9 Health)\n(4) Flee (You may or may not get away)\n")
    if players_choice == "1":
        return print(f"You did {monster_health - player_attack} to the monster")
    elif players_choice == "2":
        return print(f"You did {monster_health - (player_attack * 2)} damage and took {player_health - random.randint(1, 10)} damage from the monster!")
    elif players_choice == "3":
        return print(f"Your health is now: {player_health + 9} HP")
    elif players_choice == "4":
        if flee_chance <= 3:
            return print("You successfuly ran away!")
        elif flee_chance > 3:
            return print("You have failed to run away!")
        
    
#def monsters_turn():

print("Welcome to training! First I need to know some things about you.")
player_name = input("What is your name?\n")
fighter_class = input("What class of fighter are you?\n(1) Fighter\n(2) Mage\n(3) Rogue\nType the corresponding number\n")

print("Great, here are your stats!")

# Fighter Class
if fighter_class == "1":
    player_health = 30
    player_defense = 20
    player_attack = random.randint(1, 20) + 3
    player_damage = random.randint(1, 8) + 4
    print(f"Health: {player_health}\nDefense: {player_defense}\nAttack: {player_attack}\nDamage: {player_damage}")
# Mage Class
elif fighter_class == "2":
    player_health = 30
    player_defense = 15
    player_attack = random.randint(1, 20) + 6
    player_damage = random.randint(1, 8) + 7
    print(f"Health: {player_health}\nDefense: {player_defense}\nAttack: {player_attack}\nDamage: {player_damage}")
# Rogue Class
elif fighter_class == "3":
    player_health = 30
    player_defense = 25
    player_attack = random.randint(1, 20) + 5
    player_damage = random.randint(1, 8) + 2
    print(f"Health: {player_health}\nDefense: {player_defense}\nAttack: {player_attack}\nDamage: {player_damage}")
else:
    print("That is not an option!")

print("You are being attacked by a Dire Wolf!")

attacker = "1"
if attacker == "1":
    players_turn()
