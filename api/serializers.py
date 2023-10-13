from rest_framework import serializers

from books.models import Books


class BooksListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing books with limited fields.

    Attributes:
    model (Books): The model to use for serialization, which is the "Books" model.
    fields (list of str): The fields to include in the serialized data, including "title," "year," and "description."
    """

    class Meta:
        model = Books
        fields = ["title", "year", "description"]


class BookDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying detailed information about a book.

    Attributes:
    model (Books): The model to use for serialization, which is the "Books" model.
    fields (str): Include all fields of the model.
    """

    class Meta:
        model = Books
        fields = "__all__"
