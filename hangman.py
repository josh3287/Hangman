import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word
    
def hangman():
  
    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set() #keep track of user guess
    alphabet = set(string.ascii_uppercase)
    while len(word_letters) > 0:
        print("You have used the following letters: ", "".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word ]
        print('Current word: ', "".join(word_list))
    user_letters = input("Guess a letter: ").upper()
    if user_letters in alphabet - used_letters:
        used_letters.add(user_letters)
        if user_letters in word_letters:
            word_letters.remove(user_letters)
    if user_letters in used_letters:
        print('You already used that character. Please try again')
    else:
        quit

hangman()
    