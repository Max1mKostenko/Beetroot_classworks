class LibraryItem:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available


class Book(LibraryItem):
    def __init__(self, title, author, available, quantity_pages, issues, average_rating):
        super().__init__(title, author, available)
        self.quantity_pages = quantity_pages
        self.issues = issues
        self.average_rating = average_rating

    def book_info(self):
        return f"The book '{str(self.title).capitalize()}'\n" \
               f"Author: {str(self.author).capitalize()}\n" \
               f"Availability: {self.available}\n" \
               f"Quantity of pages: {self.quantity_pages}\n" \
               f"Issues: {self.issues}\n" \
               f"Average Rating: {self.average_rating}/5"


class DVD(LibraryItem):
    def __init__(self, title, author, available, ):
        super().__init__(title, author, available)

#
#
# class Magazine(LibraryItem):
#     def __init__(self, title, author, available, ):
#         super().__init__(title, author, available)


book = Book("The Enigma of Shadows", "A. R. Sterling", "Available", 352, "Limited stock, only 10 copies remaining", 4.2)
print(book.book_info())
