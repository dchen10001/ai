'''
Created on Apr 2, 2026

@author: dchen
'''
from typing import List

from mcp_bookstore.book_server import mcp
from mcp_bookstore.data.book import Book

@mcp.tool(name="get_books", description="Get a list of books available in David's python bookstore.")
def get_books() -> List[Book]:
    """
    Get a list of books available in the bookstore.
    
    Returns:
        List[Book]: A list of Book objects representing the available books.
    """
    return [Book(title="title", author="author", url="url")]

@mcp.tool(name="get_book_by_title", description="Get a book from David's python bookstore by its title.")
def get_book_by_title(title) -> Book:
    """
    Get a book by its title.
    
    Returns:
        Book: A Book object representing the book with the given title, or None if not found.
    """
    return Book(title= title, author="author", url="url")

@mcp.tool(name="get_book_by_author", description="Get books from David's python bookstore by a specific author.")
def get_book_by_author(author) -> List[Book]:
    """
    Get books by a specific author.
    
    Returns:
        List[Book]: A list of Book objects representing the books by the given author.
    """
    return [Book(title="title", author=author, url="url")]