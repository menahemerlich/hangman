from data.words_list import words
from hangman.words import choose_secret_word
from hangman.game import init_state, validate_guess



ch = input("Enter a ch: ")
game_info = init_state(choose_secret_word(words), max_tries=5)
print(validate_guess(ch, game_info["guessed"]))