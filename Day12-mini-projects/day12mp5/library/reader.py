import os
from . import config  # relative import

def open_ebook(file_name):
    path = os.path.join(config.EBOOK_DIR, file_name)
    if os.path.exists(path):
        return f"Opening {file_name}..."
    return "Ebook not found."
