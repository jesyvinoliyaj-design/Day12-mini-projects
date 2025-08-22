import re
import string

def clean_text(text: str) -> str:
    """Remove extra spaces and normalize text."""
    return " ".join(text.strip().split())

def remove_punctuation(text: str) -> str:
    """Remove punctuation from text."""
    return text.translate(str.maketrans("", "", string.punctuation))

def tokenize(text: str) -> list[str]:
    """Split text into words (tokens)."""
    return re.findall(r"\b\w+\b", text.lower())
