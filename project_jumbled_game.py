########## Project - Jumbled Game #############
"""
A word jumble is a word puzzle game that presents the player with a bunch of mixed up letters and requires them to unscramble the letters to find the hidden word.
The computer will take word and jumble it (mix up the letters).
Then the player will guess what the word is
"""
import random

lista = ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
word = random.choice(lista)
computer = "".join(random.sample(word, len(word)))
print("############# Welcome to Jumbled Game #############","\n")
print("We will present you a bunch of mixed up letters.")
print("Try to unscramble the letters to find the hidden word.", "\n")
print(f"Guess this word? {computer}")

n = 3 # number of guesses

while n >0:
    n -= 1
    user = input("your answer: ")
    if word == user:
        print(f"You win. The word is {word}. Congratulations!")
        break
    else:
        print("You loose. Try again")
        print(f"You have {n} tries left.")

"""
output:
############# Welcome to Jumbled Game ############# 

We will present you a bunch of mixed up letters.
Try to unscramble the letters to find the hidden word. 

Guess this word? rtafhe
your answer: father
You win. The word is father. Congratulations!
"""