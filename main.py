from data.words_list import words, words2
from hangman.words import choose_secret_word
from hangman.game import init_state, validate_guess, apply_guess, is_lost, is_won
from hangman.io import prompt_guess, print_status, print_result, render_display



def play(words: list[str]) -> None:
    word = choose_secret_word(words)
    state = init_state(word, max_tries=6)
    print(f"The word to guess: {render_display(state)}")
    while not is_lost(state) and not is_won(state):
        ch = prompt_guess()
        if validate_guess(ch, state["guessed"])[0]:
            if apply_guess(state, ch):
                print("You succeeded!!")
            else:
                print("You didn't succeed!")
            if not is_won(state):
                print_status(state)
    print_result(state)
if __name__ == "__main__":
    play(words)


