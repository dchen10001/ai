from typing import List, Optional

from mcp_bookstore.data.book import Book
from mcp_bookstore.utils.book_reader import read_books

class BookRepository:
    """
    Repository class for managing Book data with caching.
    """
    
    _books: Optional[List[Book]] = None
    
    @classmethod
    def get_books(cls) -> List[Book]:
        """
        Get all books, loading from file if not already cached.
        
        Returns:
            List[Book]: A list of all Book objects.
        """
        if cls._books is None:
            cls._books = read_books()
        return cls._books
    
    @classmethod
    def get_book_by_title(cls, title: str) -> Optional[Book]:
        """
        Get a book by its title.
        
        Args:
            title: The title of the book to find.
            
        Returns:
            Book: The Book object if found, None otherwise.
        """
        books = cls.get_books()
        for book in books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    @classmethod
    def get_books_by_author(cls, author: str) -> List[Book]:
        """
        Get all books by a specific author.
        
        Args:
            author: The author name to search for.
            
        Returns:
            List[Book]: A list of Book objects by the given author.
        """
        books = cls.get_books()
        return [book for book in books if book.author.lower() == author.lower()]
    
    @classmethod
    def clear_cache(cls) -> None:
        """
        Clear the cached books, forcing a reload on next access.
        """
        cls._books = None
