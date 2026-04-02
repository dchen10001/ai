package com.mcp.bookstore;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mcp.bookstore.service.McpBookServiceImpl;
import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class BookstoreApplication {

	public static void main(String[] args) {
		SpringApplication.run(BookstoreApplication.class, args);
	}

	@Bean
	public ObjectMapper objectMapper() {
		return new ObjectMapper();
	}

	@Bean
	public ToolCallbackProvider bookstoreTools(McpBookServiceImpl mcpBookService) {
		return MethodToolCallbackProvider.builder()
				.toolObjects(mcpBookService)
				.build();
	}
}
