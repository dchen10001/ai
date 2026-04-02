# Prompts

1. create a record, named com.mcp.bookstore.dto.Book, which has three attributes: title, author, description, and url

2. create json file, books.json under src/main/resources, which contains 5 books, including title, author, description, and url.

3. create a read utility under com.mcp.bookstore.util to read data/books.json file, and covert it to a list of Book class, and return it.

4. create a test case of the utility under test/com.mcp.bookstore.util, with Junit 5, test coverage should be 100% for the read utility.

5. Create interface McpBookService, it has three methods:
	getAllBooks(), return a list of Book	
	getBookByTitle(String title), return the first book, matched title
	getBookByAuthor(String author), return List<Book>, matched author.

6. Create a implentation of McpBookService, named McpBookServiceImpl, it implements the three methods, and delegate to the read utility to cache data.

7. create a test case of McpBookServiceImpl and put it under test/com.mcp.bookstore.service with Junit 5, test coverage should be 100% for the three methods.

8. add mcp tool annotation to three methods of McpBookServiceImpl

9. register McpBookServiceImpl to mcp tool

7. create a book_service.py, it contains a global variable of BookService class, and three methods: get_books(), find_books_by_title(title) and find_books_by_author(author),
which delgate to BookRepository class to get the data.

8. if build error due to No qualifying bean of type ObjectMapper, ask Copilot to add ObjectMapper.

9. add mcp server version as 0.0.1 to application.properties, and turn off banner, and console output.
