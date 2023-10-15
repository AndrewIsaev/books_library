from django.contrib import admin

from books.models import Authors, Books


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    """
    Custom admin class for managing books in the Django admin panel.

    This class allows administrators to view and manage books, including creating,
    editing, and deleting book records.
    """


@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    """
    Custom admin class for managing authors in the Django admin panel.

    This class allows administrators to view and manage author records, including
    creating, editing, and deleting author entries.
    """
