from django.contrib import admin

from core.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Custom admin class for managing user records in the Django admin panel.

    This class allows administrators to view and manage user records, including
    creating, editing, and deleting user entries. It is used for managing user
    accounts within the application.

    Attributes:
        None.

    Methods:
        None.
    """
