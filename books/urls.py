"""
URL configuration for book_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from books.views import (
    BooksCreateView,
    BooksDeleteView,
    BooksDetailView,
    BooksListView,
    BooksUpdateView,
    CommentCreateView,
    AuthorCreateView,
)

app_name = "books"

urlpatterns = [
    path("", BooksListView.as_view(), name="books-list"),
    path("create", BooksCreateView.as_view(), name="books-create"),
    path("<int:pk>", BooksDetailView.as_view(), name="books-detail"),
    path("<int:pk>/delete", BooksDeleteView.as_view(), name="books-delete"),
    path("<int:pk>/update", BooksUpdateView.as_view(), name="books-update"),
    path("authors/create", AuthorCreateView.as_view(), name="author-create"),
    path(
        "<int:book_id>/comment/",
        CommentCreateView.as_view(),
        name="books-comment-create",
    ),
]
