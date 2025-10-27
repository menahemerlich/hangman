import random

def choose_secret_word(words: list[str]) -> str:
    choice = random.randint(0, len(words) - 1)
    secret = words[choice]
    return secret