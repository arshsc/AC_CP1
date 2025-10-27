# AC 2nd Combat Program

import random
def newgame():

    monster_health = 50
    monster_damage = random.randint(1, 10) + 8
    flee_chance = random.randint(1, 4)
    successful_flee = False


    players_choice = input("What would you like to do?\n(1) Normal Attack\n(2) Wild Attack (2x Damage but you will also take damage\n(3) Drink a healing potion (+9 Health)\n(4) Flee (You may or may not get away)\n")
    
    def monsters_turn():
        return print(f"The monster did {player_health - monster_damage} damage to you!\nYour health is now {player_health}")

    

    print(f"Welcome to training! First I need to know some things about you.")
    player_name = input("What is your name?\n")
    fighter_class = input(f"What class of fighter are you, {player_name}?\n(1) Fighter\n(2) Mage\n(3) Rogue\nType the corresponding number\n")

    print("\nGreat, here are your stats!")

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

    attacker = random.randint(1, 2)
    if attacker == 1:
        print("\nIt's your turn!\n")
        while player_health > 0 and monster_health > 0:
        
            if players_choice == "1" and player_attack > player_defense:
                monster_health -= player_attack
                print(f"The monster's health is now {monster_health}HP")
            elif players_choice == "2" and player_attack > player_defense:
                monster_health -= (player_attack * 2)
                player_health -= random.randint(1, 10)
                print(f"The monster's health is now {monster_health}, but your health is now {player_health}")
            elif players_choice == "3":
                player_health += 9
                print(f"Your health is now: {player_health} HP")
            elif players_choice == "4":
                if flee_chance <= 3:
                    print("You successfuly ran away!")
                elif flee_chance > 3:
                    print("You have failed to run away!")
    elif attacker == 2:
        print("\nIt's the monsters turn!\n")
        while True:
            monsters_turn()
            if player_health <= 0:
                print("You lost!")
            break


newgame()