from django.contrib import admin
from books.models import Authors, Books


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    pass


@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    pass
