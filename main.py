from data.words_list import words
from hangman.words import choose_secret_word
from hangman.game import init_state, validate_guess, apply_guess, is_won, is_lost, render_display



ch = input("Enter a ch: ")
state = init_state(choose_secret_word(words), max_tries=5)
validate_guess(ch, state["guessed"])
print(state)
print(apply_guess(state, ch))
print(state)
print(is_won(state))
print(is_lost(state))
print(render_display(state))