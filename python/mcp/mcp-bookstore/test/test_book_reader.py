import pytest

from mcp_bookstore.utils.book_reader import read_books
from mcp_bookstore.data.book import Book


class TestBookReader:
    """Test cases for book_reader module."""

    def test_read_books_returns_list(self):
        """Test that read_books returns a list."""
        books = read_books()
        assert isinstance(books, list)

    def test_read_books_returns_book_objects(self):
        """Test that read_books returns Book objects."""
        books = read_books()
        assert len(books) > 0
        for book in books:
            assert isinstance(book, Book)

    def test_read_books_has_expected_count(self):
        """Test that the correct number of books is loaded."""
        books = read_books()
        assert len(books) == 5

    def test_book_has_required_attributes(self):
        """Test that each book has title, author, and url attributes."""
        books = read_books()
        for book in books:
            assert hasattr(book, 'title')
            assert hasattr(book, 'author')
            assert hasattr(book, 'url')

    def test_book_attributes_are_strings(self):
        """Test that book attributes are strings."""
        books = read_books()
        for book in books:
            assert isinstance(book.title, str)
            assert isinstance(book.author, str)
            assert isinstance(book.url, str)

    def test_first_book_is_pride_and_prejudice(self):
        """Test that the first book is Pride and Prejudice."""
        books = read_books()
        first_book = books[0]
        assert first_book.title == "Pride and Prejudice"
        assert first_book.author == "Jane Austen"
        assert "gutenberg.org" in first_book.url

    def test_books_contain_expected_titles(self):
        """Test that all expected book titles are present."""
        books = read_books()
        titles = [book.title for book in books]
        expected_titles = [
            "Pride and Prejudice",
            "Don Quixote",
            "The Big Bang Theory",
            "Moby-Dick",
            "Wuthering Heights"
        ]
        for expected_title in expected_titles:
            assert expected_title in titles