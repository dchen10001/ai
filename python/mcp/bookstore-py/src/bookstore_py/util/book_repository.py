from typing import List, Optional

from bookstore_py.data.book import Book
from bookstore_py.util.book_reader import read_books


class BookRepository:
    """
    Repository class for managing Book data with caching.
    """
    
    _books: Optional[List[Book]] = None
    
    @classmethod
    def _load_books(cls) -> None:
        """
        Load books from file using read_books() method.
        """
        if cls._books is None:
            cls._books = read_books()
    
    @classmethod
    def get_books(cls) -> List[Book]:
        """
        Get all books, loading from file if not already cached.
        
        Returns:
            List[Book]: A list of all Book objects.
        """
        cls._load_books()
        return cls._books
    
    @classmethod
    def find_books_by_title(cls, title: str) -> Optional[Book]:
        """
        Find the first book that matches the given title.
        
        Args:
            title: The title of the book to find.
            
        Returns:
            Book: The first Book object that matches, None if not found.
        """
        cls._load_books()
        for book in cls._books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    @classmethod
    def find_books_by_author(cls, author: str) -> List[Book]:
        """
        Find all books by a specific author.
        
        Args:
            author: The author name to search for.
            
        Returns:
            List[Book]: A list of Book objects by the given author.
        """
        cls._load_books()
        return [book for book in cls._books if book.author.lower() == author.lower()]
    
    @classmethod
    def clear_cache(cls) -> None:
        """
        Clear the cached books, forcing a reload on next access.
        """
        cls._books = None
