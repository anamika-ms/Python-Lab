class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name

    def display_publisher(self):
        print(f"Publisher ID: {self.publisher_id}")
        print(f"Publisher Name: {self.publisher_name}")

class Book(Publisher):
    def __init__(self, publisher_id, publisher_name, title, author):

        super().__init__(publisher_id, publisher_name)
        self.title = title
        self.author = author

    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Python(Book):
    def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
        super().__init__(publisher_id, publisher_name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display_python_book(self):
        print(f"Price: {self.price}")
        print(f"Number of Pages: {self.no_of_pages}")


if __name__ == "__main__":
    publisher_id = input("Enter Publisher ID: ")
    publisher_name = input("Enter Publisher Name: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    price = float(input("Enter Book Price: "))
    no_of_pages = int(input("Enter Number of Pages: "))

    print()
    python_book = Python(publisher_id, publisher_name, title, author, price, no_of_pages)
    python_book.display_publisher()
    python_book.display_book()
    python_book.display_python_book()

