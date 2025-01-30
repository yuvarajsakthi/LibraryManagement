import uuid

class Library:
    def __init__(self):
        self.books = {'A': 5, 'B': 3, 'C': 10, 'D': 2}
        self.customers = {}  # Key: customer_id, Value: customer details

    def display_books(self):
        print("\nBooks in Library:")
        for book, qty in self.books.items():
            print(f"{book}: {qty}")

    def register_customer(self):
        name = input("Enter your name: ")
        phone_no = input("Enter your phone number: ")
        
        for customer_id, customer in self.customers.items():
            if customer['phone_no'] == phone_no:
                print(f"Welcome back, {customer['name']}! Your borrowed books: {customer['book_list']}")
                return customer_id
        
        customer_id = str(uuid.uuid4())  # Generate a unique ID
        self.customers[customer_id] = {'name': name, 'phone_no': phone_no, 'book_list': []}
        print(f"Registration successful! Your customer ID: {customer_id}")
        return customer_id

    def borrow_book(self, customer_id, book_name):
        customer = self.customers[customer_id]
        
        if len(customer['book_list']) >= 3:
            print("You have already borrowed 3 books. Return one to borrow another.")
        elif book_name not in self.books or self.books[book_name] == 0:
            print("This book is not available in the library.")
        elif book_name in customer['book_list']:
            print("You have already borrowed this book.")
        else:
            customer['book_list'].append(book_name)
            self.books[book_name] -= 1
            print(f"You have successfully borrowed {book_name}.")

    def return_book(self, customer_id, book_name):
        customer = self.customers[customer_id]
        
        if book_name not in customer['book_list']:
            print("You did not borrow this book.")
        else:
            customer['book_list'].remove(book_name)
            self.books[book_name] += 1
            print(f"Book {book_name} returned successfully.")

    def main(self):
        while True:
            print("\n1. Register/Login\n2. Display Books\n3. Borrow Book\n4. Return Book\n5. Exit")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                customer_id = self.register_customer()
            elif choice == 2:
                self.display_books()
            elif choice == 3:
                if 'customer_id' not in locals():
                    print("Please register/login first.")
                    continue
                book_name = input("Enter book name to borrow: ")
                self.borrow_book(customer_id, book_name)
            elif choice == 4:
                if 'customer_id' not in locals():
                    print("Please register/login first.")
                    continue
                book_name = input("Enter book name to return: ")
                self.return_book(customer_id, book_name)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Try again.")

library = Library()
library.main()
