from data.words_list import words
from hangman.words import choose_secret_word
from hangman.game import init_state, validate_guess, apply_guess, is_lost, is_won
from hangman.io import prompt_guess, print_status, print_result



def play() -> None:
    word = choose_secret_word(words)
    state = init_state(word, max_tries=6)
    while not is_lost(state) and not is_won(state):
        ch = prompt_guess()
        if validate_guess(ch, state["guessed"])[0]:
            apply_guess(state, ch)
            if not is_won(state):
                print_status(state)
    print_result(state)


play()

# ch = prompt_guess()
#state = init_state(choose_secret_word(words), max_tries=5)
# validate_guess(ch, state["guessed"])
# print(state)
# print(apply_guess(state, ch))
# print(state)
# # print(is_won(state))
# # print(is_lost(state))
# print(render_display(state))
# # print(render_summary(state))
# print_status(state)
#print(state["secret"][0])
