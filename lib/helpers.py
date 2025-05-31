from lib.models import SessionLocal
from lib.models.user import User
from lib.models.book import Book
from lib.models.review import Review
from tabulate import tabulate
from sqlalchemy.orm import joinedload

def create_user(username, email):
    session = SessionLocal()
    existing = session.query(User).filter((User.username == username) | (User.email == email)).first()
    if existing:
        session.close()
        print("User with that username or email already exists.")
        return
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print(f"Created user: {user}")
    session.close()

def list_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    if not users:
        print("No users found.")
        return
    print(tabulate([(u.id, u.username, u.email) for u in users], headers=["ID", "Username", "Email"]))
    
def delete_user(user_id):
    session = SessionLocal()
    user = session.query(User).get(user_id)
    if not user:
        print(f"No user found with ID {user_id}.")
        session.close()
        return
    session.delete(user)
    session.commit()
    print(f"Deleted user with ID {user_id}.")
    session.close()


def create_book(title, author):
    session = SessionLocal()
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    print(f"Created book: {book}")
    session.close()

def list_books():
    session = SessionLocal()
    books = session.query(Book).all()
    session.close()
    if not books:
        print("No books found.")
        return
    print(tabulate([(b.id, b.title, b.author) for b in books], headers=["ID", "Title", "Author"]))

def create_review(user_id, book_id, content, rating):
    session = SessionLocal()
    user = session.query(User).get(user_id)
    book = session.query(Book).get(book_id)
    if not user or not book:
        print("Invalid user or book ID.")
        session.close()
        return
    review = Review(content=content, rating=rating, user=user, book=book)
    session.add(review)
    session.commit()
    print(f"Created review: {review}")
    session.close()

def list_reviews():
    session = SessionLocal()
    reviews = session.query(Review).options(
        joinedload(Review.user),
        joinedload(Review.book)
    ).all()
    session.close()

    if not reviews:
        print("No reviews found.")
        return

    table = [(r.id, r.user.username, r.book.title, r.rating, r.content) for r in reviews]
    print(tabulate(table, headers=["ID", "User", "Book", "Rating", "Content"]))
def exit_program():
    print("Goodbye!")
    exit()

def invalid_choice():
    print("Invalid choice. Please try again.")
