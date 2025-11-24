# Magazine Domain – Beginner Friendly Implementation

This project implements three classes:

- **Author**
- **Magazine**
- **Article**

These follow the relationships:

- An Author has many Articles
- A Magazine has many Articles
- Articles belong to ONE Author and ONE Magazine
- Author and Magazine are many-to-many THROUGH Article

---

## 🚀 How to Run

1. Install dependencies:

pipenv install
pipenv shell

markdown
Copy code

2. Run tests:

pytest

markdown
Copy code

3. Test manually:

python debug.py

markdown
Copy code

---

## 📂 Files

- `author.py` → Author class
- `magazine.py` → Magazine class
- `article.py` → Article class
- `debug.py` → for testing
- `README.md` → project documentation

---

## ✔ Features Implemented

### Author
- Read-only `name`
- `articles()`
- `magazines()`
- `add_article()`
- `topic_areas()`

### Magazine
- Editable `name` and `category`
- `articles()`
- `contributors()`
- `article_titles()`
- `contributing_authors()`
- `top_publisher()` (class method)

### Article
- Read-only `title`
- Changeable `author`
- Changeable `magazine`
- Tracks all articles globally

---
