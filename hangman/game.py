
def init_state(secret: str, max_tries: int) -> dict:
    game_info = {}
    game_info["secret"] = secret
    game_info["display"] = "_" * len(secret)
    game_info["guessed"] = []
    game_info["wrong_guesses"] = None
    game_info["max_tries"] = max_tries

    return  game_info