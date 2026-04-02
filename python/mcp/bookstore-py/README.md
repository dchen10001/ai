# MCP Book Store Server
Open command to create python project with uv
1. uv init --package bookstore-py
2. cd bookstore-py
3. uv venv
4. uv add "mcp[cli]"
5. create test folder for unit test code
   cd bookstore-py\src\bookstore-py
   create folder data, service, util 
   
6. Import project to Eclipse
   select python.exe under .venv\Script as Python interpreter
   create a PyDev Project, 
   project name: bookstore-py
   Uncheck "Use default"
   Directory: bookstore-py
   check create 'src' folder and add it to the PYTHONPATH
   
7. In Eclipse, open Github copilot chat, use the above prompts to create code step by step

8. configure MCP server in Eclipse (it can be configured in VS, Claude Desktop App as well)
   click edit preferences icon of Copilot Chat (the gear icon on the top right corner of the chat window),
   select Model Context Protocol(MCP Server), click add server, input server name and port, click save.
   
   	"py_book_server": {
		"type": "stdio",
		"command": "uv",
		"args": [
			"--directory", 
			"C:/development/claude/source/ai/python/mcp/bookstore-py/src",				
			"run",
			"bookstore_py/main.py"
		]
	}
	
	In MCP output window, you should see the server is running, and it will print the log when you call the API in next step.
	
9. Test the server
   
   MCP servers using stdio transport communicate via stdin/stdout, not HTTP.
   Use one of the following methods to test:
   
   Option 1: Use MCP Inspector (Recommended)
   ```
   cd bookstore-py
   npx @modelcontextprotocol/inspector uv --directory src run bookstore_py/main.py
   ```
   This opens a web UI to test MCP tools interactively.
   
   Option 2: Test via Copilot Chat in Eclipse
   After configuring the MCP server, ask Copilot:
   - "Get a list of books available in david's bookstore"
   - "Get book by title 1984 from david's bookstore"
   - "Get books by author Jane Austen from david's bookstore"
   
   Option 3: Test the service directly with Python
   ```
   cd bookstore-py
   uv run python -c "from bookstore_py.service.book_service import book_service; print(book_service.get_books())"
   ```