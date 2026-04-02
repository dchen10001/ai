"""
MCP Book Server - Exposes bookstore functionality via MCP protocol.
"""
from mcp.server.fastmcp import FastMCP

# Instantiate FastMCP server
mcp = FastMCP("bookstore")
