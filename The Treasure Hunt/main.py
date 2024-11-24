import random
from treasure_art import treasure

print(treasure[0])

print("Welcome to The Treasure Hunt.")
print("Your mission is to find the treasure buried on a mysterious island.")
start = input('You\'ve arrived on a remote island. Where do you want to go?'
              'Type "forest" to explore the island, or "beach" to explore the shoreline. \n').lower()
if start == "forest":
    path = input('You\'ve entered the forest and find two paths.'
                 'One path leads to a dark cave, and the other to a worn down bridge.'
                 'Type "cave" to explore the cave. '
                 'Type "bridge" to cross the bridge.\n').lower()
    if path == "cave":
        chest = input('Inside the cave, you find three chests with instructions telling you only one is real.'
                     'Chest one has a skull on it, chest two has an X symbol, and chest three has a key symbol.'
                     'Which lock will you open?\n').lower()
        if chest == "skull":
            print("It was a trap! The chess exploded! Game Over.")
        elif chest == "x":
            print("You found treasure! Congratulations! You Win!")
        elif chest == "key":
            print("The chest is empty. Better luck next time. Game Over.")
        else:
            print("Game Over.")

    else:
        print("The bridge breaks under your weight and you fall into the river. Game Over.")

else:
    print("You search the beach and get caught in quicksand. Game Over")