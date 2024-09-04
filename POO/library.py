class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor
        self.avaible = True
        
    def borrow(self):
        if self.avaible:
            self.avaible = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no esta disponible")
            
    def return_book(self):
        self.avaible = True
        print(f"El libro {self.title} ha sido devuelto")
        

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.avaible:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no esta disponible")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no ha sido prestado")
            
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        
    def add_book(self, book):
        self.books.append(book)
        print (f"Libro {book.title} agregado a la biblioteca")
        
    def register_user(self, user):
        self.users.append(user)
        print(f"Usuario {user.name} registrado")
        
    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.avaible:
                print(f"{book.title} - {book.autor}")
 
#Crear los libros                
book1 = Book("El principito", "Antoine de Saint-Exupéry")
book2 = Book("1984", "George Orwell")

#create users
user1= User("carli", "001")

#create library
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#mostrar libros
library.show_available_books()

#realizar prestamo
user1.borrow_book(book1)

#mostrar libros
library.show_available_books()

#devolver libro
user1.return_book(book1)

#mostrar libros
library.show_available_books()

