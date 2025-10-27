from .game import render_display

def prompt_guess() -> str:
    ch = input("Enter your guess: ")
    return ch

def print_status(state: dict) -> None:
    print(f"Your failed guesses: {state["guessed"]}")
    print(f"You have left {state["max_tries"] - state["wrong_guesses"]} guesses")
    print(f"Your word status: {render_display(state)}")


def print_result(state: dict) -> None:
    display = render_display(state)
    if state["secret"] == display:
        print(f"You won!!\n"
              f"the word is {state["secret"]}\n"
              f"Your guesses {state["guessed"]}")

    else:
        print(f"You lost!!\n"
              f"the word is {state["secret"]}\n"
              f"Your guesses {state["guessed"]}")







