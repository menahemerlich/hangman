
def init_state(secret: str, max_tries: int) -> dict:
    state = {}
    state["secret"] = secret
    state["display"] = ["_"] * len(secret)
    state["guessed"] = []
    state["wrong_guesses"] = 0
    state["max_tries"] = max_tries

    return  state

def validate_guess(ch: str, guesses: list[str]) -> tuple[bool, str]:
    if len(ch) == 1 and ch.isalpha() and ch not in guesses:
        return True, ch
    return False, ch

def apply_guess(state: dict, ch: str):
    i = -1
    if ch in state["secret"]:
        for j in state["secret"]:
            i += 1
            if ch == j:
                state["display"][i] = ch

        return True
    state["guessed"].append(ch)
    state["wrong_guesses"] += 1
    return False

def is_won(state: dict) -> bool:
    if "_" in state["display"]:
        return False
    return True

def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    return False

def render_display(state: dict) -> str:
    display = ""
    for i in state["display"]:
        display += i
    return display

def render_summary(state: dict) -> list[str]:
    summary = []
    summary.append(state["secret"])
    summary.append(state["guessed"][:])
    return summary

