# AC 2nd Final Project Text Adventure Game

import random

inventory = {
    "Weapons": {
        "Dagger": 10
    },
    "Consumables": {
        "Bandage": 10,
        "Energy Drink": 5
    },
    "Keys": [],
    "Items": []
}

locations = ["Trailer Home", "Collapsed House", "Mansion", "Prison", "School", "Library", "Train Station", "Entrance of the Mine", "Underground Railroad"]

player_health = 50
player_damage = random.randint(1, 10)
player_stamina = 10
#weapon_chosen = inventory["Weapons"["Dagger"]]

def intro_dialogue():

    print("\nYou heard of a rumor about an abandoned, small, ghost town 20 minutes away from your home town having valuable gems somewhere deep in the mines. No one has dared to go retrieve the valuable gems as there are spirits preventing you from going into the mines. Many deaths have been reported at this town.\n\nYou decide you want to go.\n\nYou inform your family and friends, they all try to stop you but you are determined.\n\nYou pack your bag with these items.\n\nDagger\nBandage\nEnergy Drink\nPhone\n\nYou set out and get to the town. Your adventure begins.\n\nYou arrive to the desolate town. Buildings are boarded up, the roads have a layer of sand and dirt, no one has stepped foot here in years. You take out your phone to call your family. The call rings infinitely, your phone has no service. It is just you, all alone.")

def room_input(locations):
    print("\n")
    num = 0
    for l in locations:
        num += 1
        print(f"({num}) {l}")
    location = input("\nWhere would you like to go? ")
    return location

intro_dialogue()
room_input(locations)