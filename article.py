# article.py

from author import Author
from magazine import Magazine

class Article:
    """
    Article belongs to ONE Author and ONE Magazine.
    """
    
    # Class variable to store ALL articles
    all_articles = []

    def __init__(self, author, magazine, title):
        # Validate author
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")

        # Validate magazine
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")

        # Validate title
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters")

        # Author and magazine can change later
        self._author = author
        self._magazine = magazine

        # Title is read-only (use private variable)
        self._title = title

        # Track ALL articles
        Article.all_articles.append(self)

    # -------------
    # PROPERTIES
    # -------------

    @property
    def title(self):
        """Return title of article (read-only)."""
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be type Magazine")
        self._magazine = value
