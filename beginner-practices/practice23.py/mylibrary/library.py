class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, title, author):
        self.books.append({title, author})
        
    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                return True
        return False
            
    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return book
        return None
    
    def show_books(self):
        return self.books