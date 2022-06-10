########## Project - Hangman Game #############
"""
The game is as follows.
Computer has a list of words.
Computer chooses a random word from the list.
The player gets 10 wrong guesses (10 turns).
The game follows this loop
    Computer prints the word character by character replacing with underscore
    those not guessed yet (initial no characters has been guessed).
    Player guesses a character.
    If character is not in word, a turn is withdrawn
    If no turns left, computer wins.
    If player has guessed all characters, player wins
"""
import random

lista = ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
word = random.choice(lista)

turns = 10
guesses = ""

print("############# Welcome to Hangman Game. #############", "\n")
print("You will have 10 guesses to guess a word.")

while turns > 0:
    guessed_all = True
    for c in word:
        if c in guesses:
            print(c, end=" ")
        else:
            print("_", end=" ")
            print(f"You have {turns} turns left.")
            guessed_all = False
    print()

    if not guessed_all:

        guess = input("Guess a char: ")
        guesses = guesses + guess
        if guess not in word:
            turns -= 1
    else:
        turns = 0

"""
output:
############# Welcome to Hangman Game. ############# 

You will have 10 guesses to guess a word.
_ _ _ _ _ _ _ _ _ _ _ 
Guess a char: c
You have 9 turns left.
_ _ _ _ _ _ _ _ _ _ _ 
Guess a char: f
You have 8 turns left.
_ _ _ _ _ _ _ _ _ _ _ 
Guess a char: e
You have 7 turns left.
_ _ _ _ _ _ _ _ _ _ _ 
Guess a char: p
p _ _ _ _ _ _ _ _ _ _ 
Guess a char: r
p r _ _ r _ _ _ _ _ _ 
Guess a char: m
p r _ _ r _ m m _ _ _ 
Guess a char: i
p r _ _ r _ m m i _ _ 
Guess a char: n
p r _ _ r _ m m i n _ 
Guess a char: og
p r o g r _ m m i n g 
Guess a char: a
p r o g r a m m i n g 
"""

