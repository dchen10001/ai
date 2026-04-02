from pydantic import BaseModel


class Book(BaseModel):
    """Data class representing a book in the bookstore."""
    title: str
    author: str
    description: str
    url: str
