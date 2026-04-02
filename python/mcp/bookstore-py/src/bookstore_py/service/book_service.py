from typing import List, Optional

from bookstore_py.data.book import Book
from bookstore_py.util.book_repository import BookRepository


class BookService:
    """
    Service class for book-related business logic.
    Delegates to BookRepository for data access.
    """
    
    def get_books(self) -> List[Book]:
        """
        Get all books from the repository.
        
        Returns:
            List[Book]: A list of all Book objects.
        """
        return BookRepository.get_books()
    
    def find_books_by_title(self, title: str) -> Optional[Book]:
        """
        Find a book by its title.
        
        Args:
            title: The title of the book to find.
            
        Returns:
            Book: The first Book object that matches, None if not found.
        """
        return BookRepository.find_books_by_title(title)
    
    def find_books_by_author(self, author: str) -> List[Book]:
        """
        Find all books by a specific author.
        
        Args:
            author: The author name to search for.
            
        Returns:
            List[Book]: A list of Book objects by the given author.
        """
        return BookRepository.find_books_by_author(author)


# Global instance of BookService
book_service = BookService()
