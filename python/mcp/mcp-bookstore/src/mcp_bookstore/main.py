from mcp_bookstore.book_server import mcp

import mcp_bookstore.service.mcp_book_server

if __name__ == "__main__":
    mcp.run(transport="stdio")
