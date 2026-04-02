import pytest

from mcp_bookstore.utils.book_repository import BookRepository
from mcp_bookstore.data.book import Book


class TestBookRepository:
    """Test cases for BookRepository class."""

    def setup_method(self):
        """Clear cache before each test."""
        BookRepository.clear_cache()

    def teardown_method(self):
        """Clear cache after each test."""
        BookRepository.clear_cache()

    def test_get_books_returns_list(self):
        """Test that get_books returns a list."""
        books = BookRepository.get_books()
        assert isinstance(books, list)

    def test_get_books_returns_book_objects(self):
        """Test that get_books returns Book objects."""
        books = BookRepository.get_books()
        assert len(books) > 0
        for book in books:
            assert isinstance(book, Book)

    def test_get_books_caches_result(self):
        """Test that get_books caches the result."""
        books1 = BookRepository.get_books()
        books2 = BookRepository.get_books()
        assert books1 is books2  # Same object reference

    def test_clear_cache_clears_books(self):
        """Test that clear_cache clears the cached books."""
        books1 = BookRepository.get_books()
        BookRepository.clear_cache()
        books2 = BookRepository.get_books()
        assert books1 is not books2  # Different object references after clear

    def test_get_book_by_title_found(self):
        """Test get_book_by_title returns correct book when found."""
        book = BookRepository.get_book_by_title("Pride and Prejudice")
        assert book is not None
        assert book.title == "Pride and Prejudice"
        assert book.author == "Jane Austen"

    def test_get_book_by_title_case_insensitive(self):
        """Test get_book_by_title is case insensitive."""
        book = BookRepository.get_book_by_title("pride and prejudice")
        assert book is not None
        assert book.title == "Pride and Prejudice"

    def test_get_book_by_title_not_found(self):
        """Test get_book_by_title returns None when not found."""
        book = BookRepository.get_book_by_title("Nonexistent Book")
        assert book is None

    def test_get_books_by_author_found(self):
        """Test get_books_by_author returns books by the author."""
        books = BookRepository.get_books_by_author("Jane Austen")
        assert len(books) > 0
        for book in books:
            assert book.author == "Jane Austen"

    def test_get_books_by_author_case_insensitive(self):
        """Test get_books_by_author is case insensitive."""
        books = BookRepository.get_books_by_author("jane austen")
        assert len(books) > 0
        for book in books:
            assert book.author == "Jane Austen"

    def test_get_books_by_author_not_found(self):
        """Test get_books_by_author returns empty list when author not found."""
        books = BookRepository.get_books_by_author("Unknown Author")
        assert isinstance(books, list)
        assert len(books) == 0

    def test_get_books_has_expected_count(self):
        """Test that the correct number of books is loaded."""
        books = BookRepository.get_books()
        assert len(books) == 5
