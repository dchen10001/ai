import pytest

from mcp_bookstore.service.book_service import BookService
from mcp_bookstore.data.book import Book
from mcp_bookstore.utils.book_repository import BookRepository


class TestBookService:
    """Test cases for BookService class."""

    def setup_method(self):
        """Clear repository cache before each test."""
        BookRepository.clear_cache()
        self.service = BookService()

    def teardown_method(self):
        """Clear repository cache after each test."""
        BookRepository.clear_cache()

    def test_get_all_books_returns_list(self):
        """Test that get_all_books returns a list."""
        books = self.service.get_all_books()
        assert isinstance(books, list)

    def test_get_all_books_returns_book_objects(self):
        """Test that get_all_books returns Book objects."""
        books = self.service.get_all_books()
        assert len(books) > 0
        for book in books:
            assert isinstance(book, Book)

    def test_get_all_books_has_expected_count(self):
        """Test that the correct number of books is returned."""
        books = self.service.get_all_books()
        assert len(books) == 5

    def test_search_by_title_found(self):
        """Test search_by_title returns correct book when found."""
        book = self.service.search_by_title("Pride and Prejudice")
        assert book is not None
        assert book.title == "Pride and Prejudice"
        assert book.author == "Jane Austen"

    def test_search_by_title_case_insensitive(self):
        """Test search_by_title is case insensitive."""
        book = self.service.search_by_title("moby-dick")
        assert book is not None
        assert book.title == "Moby-Dick"

    def test_search_by_title_not_found(self):
        """Test search_by_title returns None when not found."""
        book = self.service.search_by_title("Nonexistent Book")
        assert book is None

    def test_search_by_author_found(self):
        """Test search_by_author returns books by the author."""
        books = self.service.search_by_author("Jane Austen")
        assert len(books) > 0
        for book in books:
            assert book.author == "Jane Austen"

    def test_search_by_author_not_found(self):
        """Test search_by_author returns empty list when author not found."""
        books = self.service.search_by_author("Unknown Author")
        assert isinstance(books, list)
        assert len(books) == 0
