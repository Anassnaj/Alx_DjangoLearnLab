<<<<<<< HEAD
# Delete book
from bookshelf.models import Book
book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
=======
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.delete()
>>>>>>> origin/master
