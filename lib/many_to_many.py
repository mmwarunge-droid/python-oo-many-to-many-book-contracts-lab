class Author:
    # Class attribute to store all Author instances
    all = []

    def __init__(self, name):
        # Save the author's name
        self.name = name

        # Add this new author to the list of all authors
        Author.all.append(self)

    def contracts(self):
        # Return all contracts linked to this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Return all books linked to this author through contracts
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Create and return a new contract for this author and the given book
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Add up royalties from all of this author's contracts
        return sum(contract.royalties for contract in self.contracts())

class Book:
     # Class attribute to store all Book instances
    all = []

    def __init__(self, title):
        # Save the title for this book
        self.title = title

        # Add this new book to the list of all books
        Book.all.append(self)

    def contracts(self):
        # Return all contracts linked to this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Return all authors linked to this book through contracts
        return [contract.author for contract in self.contracts()]

class Contract:
    # Class attribute to store all Contract instances
    all = []

    def __init__(self, author, book, date, royalties):
        # Use property setters so validation happens
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add this new contract to the list of all contracts
        Contract.all.append(self)

    @property
    def author(self):
        # Return the saved author
        return self._author

    @author.setter
    def author(self, value):
        # Ensure author is an Author object
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("author must be an instance of Author")

    @property
    def book(self):
        # Return the saved book
        return self._book

    @book.setter
    def book(self, value):
        # Ensure book is a Book object
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception("book must be an instance of Book")

    @property
    def date(self):
        # Return the saved date
        return self._date

    @date.setter
    def date(self, value):
        # Ensure date is a string
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception("date must be a string")

    @property
    def royalties(self):
        # Return the saved royalties
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        # Ensure royalties is an integer
        if isinstance(value, int):
            self._royalties = value
        else:
            raise Exception("royalties must be an integer")

    @classmethod
    def contracts_by_date(cls, date):
        # Return all contracts with the given date
        return [contract for contract in cls.all if contract.date == date]