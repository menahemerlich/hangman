

def prompt_guess() -> str:
    ch = input("Enter your guess: ")
    return ch

def print_status(state: dict) -> None:
    print(state["display"])
    print(state["guessed"])
    print(state["max_tries"] - state["wrong_guesses"])









