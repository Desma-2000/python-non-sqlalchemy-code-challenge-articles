class Article:
    _articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be changed after initialization")

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article._articles if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()}) or None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [article for article in Article._articles if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
        return [author for author, count in author_count.items() if count > 2] or None


# Example Usage
if __name__ == "__main__":
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    article1 = author1.add_article(magazine1, "The Future of AI")
    article2 = author1.add_article(magazine2, "Benefits of a Balanced Diet")
    article3 = author2.add_article(magazine1, "Advancements in Robotics")

    print(author1.name)  # John Doe
    print([article.title for article in author1.articles()])  # ['The Future of AI', 'Benefits of a Balanced Diet']
    print([mag.name for mag in author1.magazines()])  # ['Tech Today', 'Health Weekly']
    print(author1.topic_areas())  # ['Technology', 'Health']

    print(magazine1.name)  # Tech Today
    print([article.title for article in magazine1.articles()])  # ['The Future of AI', 'Advancements in Robotics']
    print([contrib.name for contrib in magazine1.contributors()])  # ['John Doe', 'Jane Smith']
    print(magazine1.article_titles())  # ['The Future of AI', 'Advancements in Robotics']
    print([author.name for author in magazine1.contributing_authors()])  # None, since no author has more than 2 articles
