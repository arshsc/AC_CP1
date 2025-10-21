# AC 2nd Functions Notes

# all imports

# set global variables
num = 0
player_hp = 100
monster_hp = 100

# write functions
def add(x,y):
    return x+y

def attack(dmg, turn):
    if turn == "player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp - dmg
    



# write the rest of the code
#while num < add(5,5):
    print("Duck")
    num += 1
#print("Goose")
#print(f"Results is: {add(-57236434,9264387)}")
#total = add(3874687,328473)
#print(add(add(3.14,.85),10))
#add(42,7)

monster_hp, player_hp = attack(15, "monster")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

monster_hp, player_hp = attack(15, "player")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")