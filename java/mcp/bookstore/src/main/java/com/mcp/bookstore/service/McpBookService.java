package com.mcp.bookstore.service;

import com.mcp.bookstore.dto.Book;

import java.util.List;

public interface McpBookService {

    List<Book> getAllBooks();

    Book getBookByTitle(String title);

    List<Book> getBookByAuthor(String author);
}
