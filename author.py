# author.py

from article import Article


class Author:
    """
    Author class represents a writer who can create many articles.
    Author <--> Article is a one-to-many relationship.
    Author <--> Magazine is many-to-many THROUGH Article.
    """

    def __init__(self, name):
        # Validate name before setting it
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name must be longer than 0 characters")

        # Make name read-only by using a private attribute
        self._name = name

    @property
    def name(self):
        """Return the author's name (read-only)."""
        return self._name

    # -------------------------
    # Relationship methods
    # -------------------------

    def articles(self):
        """
        Returns a list of Article instances written by this author.
        """
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        """
        Returns a UNIQUE list of Magazine instances this author has written for.
        """
        return list({article.magazine for article in self.articles()})

    # -------------------------
    # Aggregate / Extra Methods
    # -------------------------

    def add_article(self, magazine, title):
        """
        Creates a new article for this author.
        """
        return Article(self, magazine, title)

    def topic_areas(self):
        """
        Returns unique list of categories the author has written about.
        Returns None if author has no articles.
        """
        mags = self.magazines()
        if len(mags) == 0:
            return None

        return list({mag.category for mag in mags})
