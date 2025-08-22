from .utils import tokenize

def word_count(text: str) -> int:
    return len(tokenize(text))

def char_count(text: str) -> int:
    return len(text)

def unique_word_count(text: str) -> int:
    return len(set(tokenize(text)))
