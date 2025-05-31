# Book Management CLI Application

Diagram link - https://dbdiagram.io/d/68345e5b6980ade2eb6a35c3
video - 

**Author:** Kelvin Ndunda

## Description

A command-line interface (CLI) app to manage users, books, and reviews. Users can create accounts, add books, and review them.

## Features

- Create and list users
- Create and list books
- Create and list reviews associated with users and books
- Input validation and error handling
- Persistent storage using SQLite with SQLAlchemy ORM
- Database migrations with Alembic

## Technologies Used

- Python 3.x
- SQLAlchemy ORM
- Alembic for migrations
- Pipenv for virtual environment and dependencies 
- Tabulate for formatted CLI tables

## Setup Instructions

1. Clone the repo.
2. Navigate to the project directory.
3. Install dependencies and activate environment:

   ```bash
   pipenv install
   pipenv shell

## Relationships
A User can write many Reviews (One-to-Many).

Many Users can review many books

A Book can have many Reviews (One-to-Many).

Each Review is associated with one User and one Book (Many-to-One for both relationships).