import re
from .catalog import list_ebooks  # relative import

def search_ebooks(keyword):
    ebooks = list_ebooks()
    pattern = re.compile(keyword, re.IGNORECASE)
    return [book for book in ebooks if pattern.search(book)]
