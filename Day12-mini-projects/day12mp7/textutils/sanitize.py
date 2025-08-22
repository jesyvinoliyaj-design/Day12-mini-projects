from .utils import clean_text, remove_punctuation

def sanitize_basic(text: str) -> str:
    """Clean spaces and punctuation."""
    return remove_punctuation(clean_text(text))
