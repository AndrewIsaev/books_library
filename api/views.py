from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import BookDetailSerializer, BooksListSerializer
from books.models import Books


# Create your views here.
class BooksListApiView(ListAPIView):
    """
    API view for listing books with limited fields.

    Attributes:
    queryset (QuerySet): The queryset of books, including related author information, to be serialized.
    serializer_class (serializer class): The serializer class to use for the serialization of book list.
    """

    queryset = Books.objects.select_related("author")
    serializer_class = BooksListSerializer


class BookDetailApiView(RetrieveAPIView):
    """
    API view for displaying detailed information about a book.

    Attributes:
    queryset (QuerySet): The queryset of all books to be used for retrieving detailed information.
    serializer_class (serializer class): The serializer class to use for the serialization of book details.
    """

    queryset = Books.objects.all()
    serializer_class = BookDetailSerializer
