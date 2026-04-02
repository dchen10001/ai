"""
MCP Book Service - Exposes book service methods as MCP tools.
"""
from typing import List, Optional

from bookstore_py.data.book import Book
from bookstore_py.mcp_book_server import mcp
from bookstore_py.service.book_service import book_service


@mcp.tool(name="get_books", description="Get a list of books available in david's bookstore.")
def get_books() -> List[Book]:
    """
    Get all books from the bookstore.
    
    Returns:
        List[Book]: A list of all Book objects.
    """
    return book_service.get_books()


@mcp.tool(name="get_book_by_title", description="Get a book from david's bookstore by its title.")
def get_book_by_title(title: str) -> Optional[Book]:
    """
    Get a book by its title.
    
    Args:
        title: The title of the book to find.
    
    Returns:
        Book: The first Book object that matches, None if not found.
    """
    return book_service.find_books_by_title(title)


@mcp.tool(name="get_books_by_author", description="Get books from david's bookstore by a specific author.")
def get_books_by_author(author: str) -> List[Book]:
    """
    Get books by a specific author.
    
    Args:
        author: The author name to search for.
    
    Returns:
        List[Book]: A list of Book objects by the given author.
    """
    return book_service.find_books_by_author(author)
