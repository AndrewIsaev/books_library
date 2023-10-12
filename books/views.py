# Create your views here.
from django.views.generic import DetailView, ListView

from books.models import Books


class BooksListView(ListView):
    """
        View for displaying a list of books.

        Attributes:
        model (Books): The model to use for the list view, which is the "Books" model.
        context_object_name (str): The name used to access the list of books in the template context.
        paginate_by (int): The number of books to display per page.

        Methods:
        get_queryset(): Returns the queryset of books, including related author information.

        Template Context:
        books (QuerySet): A queryset of books to be used in the template.

        Usage:
        - Create an instance of this view in your URL configuration to display a list of books.
        """
    model = Books
    context_object_name = "books"
    paginate_by = 3

    def get_queryset(self):
        """
            Return the queryset of books, including related author information.
        """
        return Books.objects.select_related("author").all()


class BooksDetailView(DetailView):
    """
       View for displaying the details of a single book.

       Attributes:
       model (Books): The model to use for the detail view, which is the "Books" model.
       context_object_name (str): The name used to access the book object in the template context.

       Template Context:
       book (Books): The book object to be used in the template.

       Usage:
       - Create an instance of this view in your URL configuration to display detailed information about a book.
       """
    model = Books
    context_object_name = "book"
