import pytest

from bookstore_py.util.book_repository import BookRepository
from bookstore_py.data.book import Book


class TestBookRepository:
    """Test cases for BookRepository class."""

    def setup_method(self):
        """Clear cache before each test."""
        BookRepository.clear_cache()

    def teardown_method(self):
        """Clear cache after each test."""
        BookRepository.clear_cache()

    # Tests for get_books()
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

    def test_get_books_has_expected_count(self):
        """Test that the correct number of books is returned."""
        books = BookRepository.get_books()
        assert len(books) == 5

    def test_get_books_caches_result(self):
        """Test that get_books caches the result."""
        books1 = BookRepository.get_books()
        books2 = BookRepository.get_books()
        assert books1 is books2  # Same object reference

    # Tests for find_books_by_title()
    def test_find_books_by_title_found(self):
        """Test find_books_by_title returns correct book when found."""
        book = BookRepository.find_books_by_title("Pride and Prejudice")
        assert book is not None
        assert book.title == "Pride and Prejudice"
        assert book.author == "Jane Austen"

    def test_find_books_by_title_case_insensitive(self):
        """Test find_books_by_title is case insensitive."""
        book = BookRepository.find_books_by_title("moby-dick")
        assert book is not None
        assert book.title == "Moby-Dick"

    def test_find_books_by_title_not_found(self):
        """Test find_books_by_title returns None when not found."""
        book = BookRepository.find_books_by_title("Nonexistent Book")
        assert book is None

    def test_find_books_by_title_returns_first_match(self):
        """Test find_books_by_title returns the first matching book."""
        book = BookRepository.find_books_by_title("1984")
        assert book is not None
        assert book.title == "1984"
        assert book.author == "George Orwell"

    # Tests for find_books_by_author()
    def test_find_books_by_author_found(self):
        """Test find_books_by_author returns books by the author."""
        books = BookRepository.find_books_by_author("Jane Austen")
        assert len(books) > 0
        for book in books:
            assert book.author == "Jane Austen"

    def test_find_books_by_author_case_insensitive(self):
        """Test find_books_by_author is case insensitive."""
        books = BookRepository.find_books_by_author("jane austen")
        assert len(books) > 0
        for book in books:
            assert book.author == "Jane Austen"

    def test_find_books_by_author_not_found(self):
        """Test find_books_by_author returns empty list when author not found."""
        books = BookRepository.find_books_by_author("Unknown Author")
        assert isinstance(books, list)
        assert len(books) == 0

    def test_find_books_by_author_returns_all_matches(self):
        """Test find_books_by_author returns all books by the author."""
        books = BookRepository.find_books_by_author("Herman Melville")
        assert len(books) == 1
        assert books[0].title == "Moby-Dick"
