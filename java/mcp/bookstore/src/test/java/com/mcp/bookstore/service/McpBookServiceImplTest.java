package com.mcp.bookstore.service;

import com.mcp.bookstore.dto.Book;
import com.mcp.bookstore.util.BookReader;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
class McpBookServiceImplTest {

    @Mock
    private BookReader bookReader;

    private McpBookServiceImpl mcpBookService;

    private List<Book> testBooks;

    @BeforeEach
    void setUp() throws IOException {
        testBooks = Arrays.asList(
                new Book("To Kill a Mockingbird", "Harper Lee", "A classic novel", "https://example.com/book1"),
                new Book("1984", "George Orwell", "A dystopian novel", "https://example.com/book2"),
                new Book("Animal Farm", "George Orwell", "A political satire", "https://example.com/book3"),
                new Book("Pride and Prejudice", "Jane Austen", "A romantic novel", "https://example.com/book4")
        );

        when(bookReader.readBooks()).thenReturn(testBooks);

        mcpBookService = new McpBookServiceImpl(bookReader);
        mcpBookService.init();
    }

    @Test
    void getAllBooks_shouldReturnAllBooks() {
        List<Book> books = mcpBookService.getAllBooks();

        assertNotNull(books);
        assertEquals(4, books.size());
        assertEquals(testBooks, books);
    }

    @Test
    void getBookByTitle_shouldReturnMatchingBook() {
        Book book = mcpBookService.getBookByTitle("1984");

        assertNotNull(book);
        assertEquals("1984", book.title());
        assertEquals("George Orwell", book.author());
    }

    @Test
    void getBookByTitle_shouldReturnMatchingBookCaseInsensitive() {
        Book book = mcpBookService.getBookByTitle("TO KILL A MOCKINGBIRD");

        assertNotNull(book);
        assertEquals("To Kill a Mockingbird", book.title());
    }

    @Test
    void getBookByTitle_shouldReturnNullWhenNotFound() {
        Book book = mcpBookService.getBookByTitle("Nonexistent Book");

        assertNull(book);
    }

    @Test
    void getBookByAuthor_shouldReturnMatchingBooks() {
        List<Book> books = mcpBookService.getBookByAuthor("George Orwell");

        assertNotNull(books);
        assertEquals(2, books.size());
        assertTrue(books.stream().allMatch(book -> "George Orwell".equals(book.author())));
    }

    @Test
    void getBookByAuthor_shouldReturnMatchingBooksCaseInsensitive() {
        List<Book> books = mcpBookService.getBookByAuthor("HARPER LEE");

        assertNotNull(books);
        assertEquals(1, books.size());
        assertEquals("Harper Lee", books.get(0).author());
    }

    @Test
    void getBookByAuthor_shouldReturnEmptyListWhenNotFound() {
        List<Book> books = mcpBookService.getBookByAuthor("Unknown Author");

        assertNotNull(books);
        assertTrue(books.isEmpty());
    }
}
