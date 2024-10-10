

import random
from hangman_words import word_list
from hangman_art import stages,logo

# #TODO 1-Randomly choose a word from word_list and assign it to a variable called word_choosen

print("Welcome to the Hangman game")
print(logo)
print('''**********************<????/7>Lives Left **********''')
word_chosen=random.choice(word_list)
lives = 6
blank = ""
for Position in range(len(word_chosen)):
    blank += "-"
print(blank)

# #TODO 2-ask the user to guess a letter and assign it into a variable called user_guess.Make a guess into lowercase

game_over = False
user_guess = []
while not game_over:
    user_guesses_letter = input("Guess the letter:").lower()
    print("your guesses:",user_guesses_letter)
# #TODO 3- check if the letter the user guessed(user_guess)is one of the letter in  word_choosen.print"Right" and "wrong" if it's not

    if user_guesses_letter in user_guess:
        print(f"your guesses letter is already guessed:-{user_guesses_letter}")

    display = ""
    for letter in word_chosen:
        if letter == user_guesses_letter:
            display += letter
            user_guess += letter
        elif letter in user_guess:
            display += letter
        else:
            display += "_"
    print(display)
    if user_guesses_letter not in word_chosen:
        print(f"you've guessed the wrong letter:-{user_guesses_letter}")
        lives -= 1

        if lives == 0:
            game_over = True
            print("******you lost")

    print(f"your remaining lives:- {lives}")

    if "_" not in display:
        game_over = True
        print("********you win")
    print(stages[abs(lives-6)])
print("correct word was :", word_chosen)