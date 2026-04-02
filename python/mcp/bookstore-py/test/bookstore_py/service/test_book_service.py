import pytest

from bookstore_py.service.book_service import book_service, BookService
from bookstore_py.data.book import Book
from bookstore_py.util.book_repository import BookRepository


class TestBookService:
    """Test cases for BookService class."""

    def setup_method(self):
        """Clear repository cache before each test."""
        BookRepository.clear_cache()

    def teardown_method(self):
        """Clear repository cache after each test."""
        BookRepository.clear_cache()

    # Tests for global book_service instance
    def test_book_service_is_instance_of_book_service_class(self):
        """Test that book_service is an instance of BookService."""
        assert isinstance(book_service, BookService)

    # Tests for get_books()
    def test_get_books_returns_list(self):
        """Test that get_books returns a list."""
        books = book_service.get_books()
        assert isinstance(books, list)

    def test_get_books_returns_book_objects(self):
        """Test that get_books returns Book objects."""
        books = book_service.get_books()
        assert len(books) > 0
        for book in books:
            assert isinstance(book, Book)

    def test_get_books_has_expected_count(self):
        """Test that the correct number of books is returned."""
        books = book_service.get_books()
        assert len(books) == 5

    # Tests for find_books_by_title()
    def test_find_books_by_title_found(self):
        """Test find_books_by_title returns correct book when found."""
        book = book_service.find_books_by_title("Pride and Prejudice")
        assert book is not None
        assert book.title == "Pride and Prejudice"
        assert book.author == "Jane Austen"

    def test_find_books_by_title_case_insensitive(self):
        """Test find_books_by_title is case insensitive."""
        book = book_service.find_books_by_title("moby-dick")
        assert book is not None
        assert book.title == "Moby-Dick"

    def test_find_books_by_title_not_found(self):
        """Test find_books_by_title returns None when not found."""
        book = book_service.find_books_by_title("Nonexistent Book")
        assert book is None

    def test_find_books_by_title_returns_first_match(self):
        """Test find_books_by_title returns the first matching book."""
        book = book_service.find_books_by_title("1984")
        assert book is not None
        assert book.title == "1984"
        assert book.author == "George Orwell"

    # Tests for find_books_by_author()
    def test_find_books_by_author_found(self):
        """Test find_books_by_author returns books by the author."""
        books = book_service.find_books_by_author("Jane Austen")
        assert len(books) > 0
        for book in books:
            assert book.author == "Jane Austen"

    def test_find_books_by_author_case_insensitive(self):
        """Test find_books_by_author is case insensitive."""
        books = book_service.find_books_by_author("jane austen")
        assert len(books) > 0
        for book in books:
            assert book.author == "Jane Austen"

    def test_find_books_by_author_not_found(self):
        """Test find_books_by_author returns empty list when author not found."""
        books = book_service.find_books_by_author("Unknown Author")
        assert isinstance(books, list)
        assert len(books) == 0

    def test_find_books_by_author_returns_all_matches(self):
        """Test find_books_by_author returns all books by the author."""
        books = book_service.find_books_by_author("Herman Melville")
        assert len(books) == 1
        assert books[0].title == "Moby-Dick"

#t = TestBookService();
#t.test_get_books_returns_book_objects()