import random

from words import words

def get_valid_words(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' or '' in word:
        word =  random.choice(words)
    
    return word.upper()