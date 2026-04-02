# Prompts

1. create a book.py under data folder, it contact data class, named Book, which has three attributes: title, author, description, and url

2. create json file, books.json, which contains 5 books, including title, author, description, and url.

3. create a read utility to read data/books.json file, and covert it to a list of Book class in book.py

4. create test case for book_reader under test/bookstore_py/test folder

5. create a book_repository.py in util folder, 
it contains BookRepository class, which uses read_book() method to load the list of books from file, 
and chach it to local variable. 
add a method get_books() to return the list of books, 
and add a method find_books_by_title(title) to find book by title, 
it should return the first book that match the title.
add a method find_books_by_author(author) to find book by author,
it should return the list of books that match the author.

6. create a test case of it and put it under test/bookstore_py/util folder, and test the get_books(), find_books_by_title(title) and find_books_by_author(author) methods.

7. create a book_service.py, it contains a global variable of BookService class, and three methods: get_books(), find_books_by_title(title) and find_books_by_author(author),
which delgate to BookRepository class to get the data.

8. create a test case of it and put it under test/bookstore_py/service folder, and test the get_books(), find_books_by_title(title) and find_books_by_author(author) methods.

9. create mcp_book_server.py under bookstore_py, it instantiates FastMCP object 

10. create main.py, it imports FastMCP and mcp_book_server, and run the server.	

11. add mcp_book_service.py under service, it has three methods: 
get_books(), return a list of Book
get_book_by_title(title), return the first book matched title
get_book_by_author(author), return a list of book, matched author.
add mcp.tool annotation to three methods.
