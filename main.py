from data.words import words
from hangman.words import choose_secret_word
from hangman.game import init_state



print(init_state(choose_secret_word(words), max_tries=5))