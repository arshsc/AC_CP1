# AC 2nd Combat Program
import random

print("Welcome to training! First I need to know some things about you!")
player_name = input("What is your name?\n")
print(f"\nWhat class of fighter are you, {player_name}?")
fighter_class = input("(1) if you are a Fighter\n(2) if you are a Mage\n(3) if you are a Rogue\n")

print("\nGreat, here are your stats!")
# Fighter
if fighter_class == "1":
    player_health = 30
    player_defense = 14
    player_damage_bonus = 4
    print(f"\nHealth: {player_health}\nDefense: {player_defense}\nAttack: D20 + 3\nDamage: D8 + 4")
# Mage
elif fighter_class == "2":
    player_health = 30
    player_defense = 12
    player_damage_bonus = 71
    print(f"\nHealth: {player_health}\nDefense: {player_defense}\nAttack: D20 + 6\nDamage: D8 + 7")
# Rogue
elif fighter_class == "3":
    player_health = 30
    player_defense = 16
    player_damage_bonus = 2
    print(f"\nHealth: {player_health}\nDefense: {player_defense}\nAttack: D20 + 5\nDamage: D8 + 2")
else:
    print("That is not an option!")


monster_name = "Dire Wolf"
monster_health = 50
monster_damage = random.randint(5, 12)
print(f"\nYou are being attacked by a {monster_name}!\n")

def player_turn(player_health, monster_health, player_damage_bonus):
    print("What would you like to do?")
    print("(1) Normal Attack")
    print("(2) Wild Attack (2x Damage but you will also take damage)")
    print("(3) Drink a healing potion (+9 Health)")
    print("(4) Flee (You may or may not get away)\n")
    choice = input("Your choice: ")

    if choice == "1":
        damage = random.randint(1, 8) + player_damage_bonus
        monster_health -= damage
        print(f"\nYou hit! You dealt {damage} damage!")
        print(f"{monster_name} now has {monster_health} Health\n")
    elif choice == "2":
        damage = (random.randint(1, 8) + player_damage_bonus) * 2
        recoil = random.randint(1, 10)
        monster_health -= damage
        player_health -= recoil
        print(f"\nWild attack! You dealt {damage} damage but hurt yourself for {recoil}!")
        print(f"{monster_name} now has {monster_health} Health")
        print(f"Your health is now {player_health}\n")
    elif choice == "3":
        player_health += 9
        print(f"\nYou drink a potion. Your health is now {player_health}.\n")
    elif choice == "4":
        flee_chance = random.randint(1, 4)
        if flee_chance <= 3:
            print("\nYou successfully ran away!\n")
            return player_health, monster_health, True
        else:
            print("\nYou failed to run away!\n")
    else:
        print("\nInvalid option. Try again.\n")

    return player_health, monster_health, False


def monster_turn(player_health, monster_damage):
    damage = random.randint(5, 12)
    player_health -= damage
    print(f"The Dire Wolf did {damage} damage to you!")
    print(f"Your health is now {player_health}\n")
    return player_health

attacker = random.randint(1, 2)
if attacker == 1:
    print("You move first!\n")
else:
    print("The Dire Wolf moves first!\n")
    player_health = monster_turn(player_health, monster_damage)

fled = False
while player_health > 0 and monster_health > 0 and not fled:
    player_health, monster_health, fled = player_turn(player_health, monster_health, player_damage_bonus)
    if fled or monster_health <= 0:
        break
    player_health = monster_turn(player_health, monster_damage)
if fled:
    print("You escaped safely!\n")
elif player_health <= 0:
    print("You were defeated!\n")
elif monster_health <= 0:
    print(f"You defeated the {monster_name}!\n")