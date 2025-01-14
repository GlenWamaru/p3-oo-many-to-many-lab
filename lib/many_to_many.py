class Author:
    _all_authors = []

    def __init__(self, name):
        self.name = name
        self._all_authors.append(self)
        self._contracts = []

    def all_authors(cls):
        return cls._all_authors

    def contracts(self):
        return [contract for contract in Contract._all_contracts if contract.author == self] 

    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, (int, float)):
            raise Exception("Invalid royalties")
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)

        return contract


    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    _all_books = []
    
    def __init__(self, title):
        self.title = title
        self._all_books.append(self)

    def all_books(cls):
        return cls._all_books    


class Contract:
    _all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self._all_contracts.append(self)

    def contracts_by_date(cls, date):
        return [contract for contract in cls._all_contracts if contract.date == date]