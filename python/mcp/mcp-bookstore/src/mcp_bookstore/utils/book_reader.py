import json
from pathlib import Path
from typing import List

from mcp_bookstore.data.book import Book


def read_books() -> List[Book]:
    """
    Read books from the books.json file and convert them to a list of Book objects.
    
    Returns:
        List[Book]: A list of Book objects loaded from the JSON file.
    """
    # Get the path to the books.json file relative to this module
    data_dir = Path(__file__).parent.parent / "data"
    books_file = data_dir / "books.json"
    
    with open(books_file, "r", encoding="utf-8") as f:
        books_data = json.load(f)
    
    books = [
        Book(
            title=book["title"],
            author=book["author"],
            url=book["url"]
        )
        for book in books_data
    ]
    
    return books
