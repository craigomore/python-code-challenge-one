# python-code-challenge-one
# Magazine Domain Project

This project implements a simple Object-Oriented Python domain consisting of **Author**, **Magazine**, and **Article** classes. The goal is to model relationships:

* An **Author** has many Articles.
* A **Magazine** has many Articles.
* An **Article** belongs to one Author and one Magazine.
* Authors and Magazines have a many‑to‑many relationship through Articles.

This implementation also includes:

* Input validation
* Relationship helper methods
* Aggregate queries
* Support for automated tests
* Clear class responsibilities and constraints

## Files

* `author.py` — Contains the Author class
* `magazine.py` — Contains the Magazine class
* `article.py` — Contains the Article class
* `debug.py` — A helper script for interactively testing your objects

## Setup

```bash
pipenv install
pipenv shell
pytest
python lib/debug.py
```

## Features

### Author

* Read‑only name
* List authored articles
* List unique magazines
* Add articles
* Topic areas (categories written in)

### Magazine

* Editable name and category
* List published articles
* List contributors
* Article titles
* Frequent contributors (2+)
* Top publisher class method

### Article

* Belongs to an author and magazine
* Valid title (read‑only)
* Tracks all instances

## Notes

* All invalid input raises `Exception()`
* Uses class‑level lists to store global state for Articles and Magazines
* Fully compatible with the provided test suite

## Debugging

Use `python lib/debug.py` to open an interactive REPL with sample objects.
