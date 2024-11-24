import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
comp = ["Rock", "Paper", "Scissors"]

if choice == "0":
    print(rock)
    comp_choice = random.choice(comp)
    if random.choice(comp) == "Rock":
        print("Computer chose:", rock)
        print("It's a draw")
    elif random.choice(comp) == "Paper":
        print("Computer chose:", paper)
        print("You lose")
    else:
        print("Computer chose:", scissors)
        print("You win")
elif choice == "1":
    print(paper)
    comp_choice = random.choice(comp)
    if random.choice(comp) == "Rock":
        print("Computer chose:", rock)
        print("You win")
    elif random.choice(comp) == "Paper":
        print("Computer chose:", paper)
        print("It's a draw")
    else:
        print("Computer chose:", scissors)
        print("You lose")
elif choice == "2":
    print(scissors)
    comp_choice = random.choice(comp)
    if random.choice(comp) == "Rock":
        print("Computer chose:", rock)
        print("You lose")
    elif random.choice(comp) == "Paper":
        print("Computer chose:", paper)
        print("You win")
    else:
        print("Computer chose:", scissors)
        print("It's a draw")
else:
    print("Input error. Please try again.")