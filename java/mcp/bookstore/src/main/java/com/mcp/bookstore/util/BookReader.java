package com.mcp.bookstore.util;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.mcp.bookstore.dto.Book;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

@Component
public class BookReader {

    private final ObjectMapper objectMapper;

    public BookReader(ObjectMapper objectMapper) {
        this.objectMapper = objectMapper;
    }

    public List<Book> readBooks() throws IOException {
        ClassPathResource resource = new ClassPathResource("books.json");
        try (InputStream inputStream = resource.getInputStream()) {
            return objectMapper.readValue(inputStream, new TypeReference<List<Book>>() {});
        }
    }
}
