from typing import List, Optional

from mcp_bookstore.data.book import Book
from mcp_bookstore.utils.book_repository import BookRepository

class BookService:
    """
    Service class for book-related business logic.
    """
    
    def __init__(self):
        self._repository = BookRepository
    
    def get_all_books(self) -> List[Book]:
        """
        Get all books from the repository.
        
        Returns:
            List[Book]: A list of all Book objects.
        """
        return self._repository.get_books()
    
    def search_by_title(self, title: str) -> Optional[Book]:
        """
        Search for a book by its title.
        
        Args:
            title: The title of the book to search for.
            
        Returns:
            Book: The Book object if found, None otherwise.
        """
        return self._repository.get_book_by_title(title)
    
    def search_by_author(self, author: str) -> List[Book]:
        """
        Search for books by author.
        
        Args:
            author: The author name to search for.
            
        Returns:
            List[Book]: A list of Book objects by the given author.
        """
        return self._repository.get_books_by_author(author)
