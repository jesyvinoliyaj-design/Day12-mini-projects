from .utils import tokenize

def most_common_word(text: str) -> str:
    tokens = tokenize(text)
    if not tokens:
        return None
    return max(set(tokens), key=tokens.count)

def word_frequency(text: str) -> dict:
    tokens = tokenize(text)
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1
    return freq
