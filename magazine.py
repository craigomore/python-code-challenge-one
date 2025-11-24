# magazine.py

from article import Article

class Magazine:
    """
    Magazine class represents a publication.
    A magazine has many articles.
    A magazine has many authors through articles.
    """

    # Class-level list to track ALL magazines (for top_publisher)
    all_magazines = []

    def __init__(self, name, category):
        # Validate name
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise Exception("Name must be between 2 and 16 characters")

        # Validate category
        if not isinstance(category, str):
            raise Exception("Category must be a string")
        if len(category) == 0:
            raise Exception("Category must be longer than 0 characters")

        self._name = name
        self._category = category

        # Save instance
        Magazine.all_magazines.append(self)

    # -----------
    # PROPERTIES
    # -----------

    @property
    def name(self):
        """Return name of magazine (can change)."""
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        """Return category of magazine (can change)."""
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value) == 0:
            raise Exception("Category must be longer than 0 characters")
        self._category = value

    # -------------------------
    # Relationship methods
    # -------------------------

    def articles(self):
        """Returns list of Article instances belonging to this magazine."""
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        """Returns unique list of authors who wrote articles for this magazine."""
        return list({article.author for article in self.articles()})

    # -------------------------
    # Aggregate / Extra Methods
    # -------------------------

    def article_titles(self):
        """Return list of article title strings OR None if none exist."""
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """
        Return authors who have written more than 2 articles for this magazine.
        """
        author_counts = {}

        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        # Filter authors who wrote > 2
        result = [author for author, count in author_counts.items() if count > 2]

        return result if result else None

    @classmethod
    def top_publisher(cls):
        """
        Returns magazine with the MOST articles.
        Returns None if no articles exist.
        """
        if len(Article.all_articles) == 0:
            return None

        # Sort by number of articles
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))
