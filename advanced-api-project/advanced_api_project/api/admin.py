from django.contrib import admin
from .models import Author, Book  # Import the models

# Optional: Customize how the Book model is displayed in the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_year', 'author')  # Example fields to display
    search_fields = ('title', 'author__name')  # Search functionality

# Register the models with the admin site
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
