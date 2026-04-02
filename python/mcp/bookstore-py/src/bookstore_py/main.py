"""
Main entry point for the MCP Bookstore server.
"""
from bookstore_py.mcp_book_server import mcp
import bookstore_py.service.mcp_book_service  # Register MCP tools

if __name__ == "__main__":
    mcp.run(transport="stdio")
