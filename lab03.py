# Lab 03 sulutions
import random

diceOptions = list(range(1, 7)) # list of numbers from 1 to 6

# List of weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"] 

# Print out the available weapons
print("Available weapons: ")
for weapon in weapons:
    print(weapon)
print("__________________________")

# Validate input integer
def validateInput(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Invalid input. Please enter a number between 1 and 6")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6")

combatStrength = validateInput("Enter your combat Strength: (Number between 1-6) ")

mCombatStrength = validateInput("Enter the monster's combat Strength: (Number between 1-6) ")
        
for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = heroRoll + combatStrength
    monsterTotal = monsterRoll + mCombatStrength

    print(f"\n Hero rolled ({heroRoll}), Monster rolled ({monsterRoll})")
    print(f"\n Hero selected weapon: {heroWeapon}, Monster selected weapon: {monsterWeapon}")
    print(f"\n Hero total strength: {heroTotal}, Monster total strength: {monsterTotal}")

    if heroTotal > monsterRoll:
        print("Hero wins round!")
    elif heroTotal < monsterRoll:
        print("Monster wins round!")
    else:
        print("It's a tie!")