
def init_state(secret: str, max_tries: int) -> dict:
    state = {}
    state["secret"] = secret
    state["display"] = "_" * len(secret)
    state["guessed"] = []
    state["wrong_guesses"] = 0
    state["max_tries"] = max_tries
    return  state

def validate_guess(ch: str, guesses: list[str]) -> tuple[bool, str]:
    if len(ch) == 1 and ch.isalpha() and ch not in guesses:
        return True, ch
    return False, ch

def apply_guess(state: dict, ch: str) -> bool:
    if ch in state["secret"]:
        return False
    state["guessed"].append(ch)
    state["wrong_guesses"] += 1
    state["max_tries"] -= 1
    return True

def is_won(state: dict) -> bool:
    if "_" in state["display"]:
        return False
    return True



