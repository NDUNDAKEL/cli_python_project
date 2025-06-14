
from lib.helpers import (
    create_user,
    list_users,
    create_book,
    list_books,
    create_review,
    list_reviews,
    exit_program,
    invalid_choice,
    delete_user,
    delete_book,
    update_user,
    update_book
)


def main_menu():
    print("\n=== Book Management CLI ===")
    print("1. Create User")
    print("2. List Users")
    print("3. Create Book")
    print("4. List Books")
    print("5. Create Review")
    print("6. List Reviews")
    print("7. Delete User")
    print("8. Update User")
    print("9. Delete Book")
    print("10. Update Book")
    print("0. Exit")

def main():
    while True:
        main_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            username = input("Username: ").strip()
            email = input("Email: ").strip()
            create_user(username, email)
        elif choice == "2":
            list_users()
        elif choice == "3":
            title = input("Book Title: ").strip()
            author = input("Author: ").strip()
            create_book(title, author)
        elif choice == "4":
            list_books()
        elif choice == "5":
            try:
                user_id = int(input("User ID: ").strip())
                book_id = int(input("Book ID: ").strip())
                content = input("Review content: ").strip()
                rating = int(input("Rating (1-5): ").strip())
                if rating < 1 or rating > 5:
                    print("Rating must be between 1 and 5.")
                    continue
                create_review(user_id, book_id, content, rating)
            except ValueError:
                print("Invalid input. IDs and rating must be integers.")
        elif choice == "6":
            list_reviews()
        elif choice == "7":  # New delete user option
            try:
                user_id = int(input("Enter User ID to delete: ").strip())
                delete_user(user_id)
            except ValueError:
                print("Invalid input. User ID must be an integer.")
        elif choice == "8":
            try:
                user_id = int(input("User ID to update: ").strip())
                new_username = input("New username (leave blank to keep current): ").strip()
                new_email = input("New email (leave blank to keep current): ").strip()
                update_user(user_id, new_username or None, new_email or None)
            except ValueError:
                print("Invalid input. User ID must be an integer.")

        elif choice == "9":
            try:
                book_id = int(input("Enter Book ID to delete: ").strip())
                delete_book(book_id)
            except ValueError:
                print("Invalid input. Book ID must be an integer.")

        elif choice == "10":
            try:
                book_id = int(input("Book ID to update: ").strip())
                new_title = input("New title (leave blank to keep current): ").strip()
                new_author = input("New author (leave blank to keep current): ").strip()
                update_book(book_id, new_title or None, new_author or None)
            except ValueError:
                print("Invalid input. Book ID must be an integer.")
        elif choice == "0":
            exit_program()
        else:
            invalid_choice()

if __name__ == "__main__":
    main()
