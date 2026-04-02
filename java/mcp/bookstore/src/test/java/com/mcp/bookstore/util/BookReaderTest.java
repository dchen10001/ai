package com.mcp.bookstore.util;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mcp.bookstore.dto.Book;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class BookReaderTest {

    private BookReader bookReader;

    @BeforeEach
    void setUp() {
        bookReader = new BookReader(new ObjectMapper());
    }

    @Test
    void readBooks_shouldReturnListOfBooks() throws IOException {
        List<Book> books = bookReader.readBooks();

        assertNotNull(books);
        assertEquals(5, books.size());
    }

    @Test
    void readBooks_shouldReturnBooksWithCorrectAttributes() throws IOException {
        List<Book> books = bookReader.readBooks();

        Book firstBook = books.get(0);
        assertNotNull(firstBook.title());
        assertNotNull(firstBook.author());
        assertNotNull(firstBook.description());
        assertNotNull(firstBook.url());
    }

    @Test
    void readBooks_shouldContainExpectedBook() throws IOException {
        List<Book> books = bookReader.readBooks();

        boolean containsExpectedBook = books.stream()
                .anyMatch(book -> "To Kill a Mockingbird".equals(book.title()) 
                        && "Harper Lee".equals(book.author()));

        assertTrue(containsExpectedBook);
    }

    @Test
    void readBooks_allBooksShouldHaveNonEmptyFields() throws IOException {
        List<Book> books = bookReader.readBooks();

        for (Book book : books) {
            assertFalse(book.title().isEmpty(), "Title should not be empty");
            assertFalse(book.author().isEmpty(), "Author should not be empty");
            assertFalse(book.description().isEmpty(), "Description should not be empty");
            assertFalse(book.url().isEmpty(), "URL should not be empty");
        }
    }
}
