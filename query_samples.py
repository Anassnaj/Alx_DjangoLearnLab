from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using related_name defined in ForeignKey
    return books

# Query 2: List all books in a specific library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using related_name defined in ManyToManyField
    return books

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Using related_name defined in OneToOneField
    return librarian
