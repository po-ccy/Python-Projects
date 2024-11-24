import random
from hangman_words import word_list
from hangman_art import logo, stages
print(logo)

word = random.choice(word_list)
print(word)

placeholder = ""
word_length = len(word)

for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

lives = 6
correct = []

while lives != 0:

    print(f"YOU HAVE {lives}/6 LIVES LEFT")
    guess = input("Guess a letter: ").lower()

    if guess in correct:
        print(f"You have already guessed {guess}, choose a different letter.")

    display = ""

    for letter in word:
        if letter == guess:
            display += letter
            correct.append(guess)
        elif letter in correct:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lose a life.")

        if lives == 0:
            print(f"You are out of lives. The word was {word}. You Lose.")
            break


    if "_" not in display:
        print("Congratulations! You guessed the word!")
        break

    print(stages[lives])
