import os
import glob
from . import config  # relative import

def list_ebooks():
    if not os.path.exists(config.EBOOK_DIR):
        os.makedirs(config.EBOOK_DIR)
    return glob.glob(os.path.join(config.EBOOK_DIR, "*.pdf"))

def add_ebook(file_path):
    if os.path.exists(file_path):
        dest = os.path.join(config.EBOOK_DIR, os.path.basename(file_path))
        os.rename(file_path, dest)
        return f"Added: {dest}"
    return "File not found."
