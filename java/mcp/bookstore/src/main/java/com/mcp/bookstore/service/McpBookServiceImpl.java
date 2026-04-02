package com.mcp.bookstore.service;

import java.io.IOException;
import java.util.List;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.ai.tool.annotation.ToolParam;
import org.springframework.stereotype.Service;

import com.mcp.bookstore.dto.Book;
import com.mcp.bookstore.util.BookReader;

import jakarta.annotation.PostConstruct;

@Service
public class McpBookServiceImpl implements McpBookService {

    private final BookReader bookReader;
    private List<Book> cachedBooks;

    public McpBookServiceImpl(BookReader bookReader) {
        this.bookReader = bookReader;
    }

    @PostConstruct
    public void init() throws IOException {
        this.cachedBooks = bookReader.readBooks();
    }

    @Override
    @Tool(description = "Get all books from the bookstore")
    public List<Book> getAllBooks() {
        return cachedBooks;
    }

    @Override
    @Tool(description = "Get a book by its title")
    public Book getBookByTitle(@ToolParam(description = "The title of the book to search for") String title) {
        return cachedBooks.stream()
                .filter(book -> book.title().equalsIgnoreCase(title))
                .findFirst()
                .orElse(null);
    }

    @Override
    @Tool(description = "Get books by author name")
    public List<Book> getBookByAuthor(@ToolParam(description = "The author name to search for") String author) {
        return cachedBooks.stream()
                .filter(book -> book.author().equalsIgnoreCase(author))
                .toList();
    }
}
