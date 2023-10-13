# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

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


class BooksCreateView(CreateView):
    """
    View for creating a new book record.

    Attributes:
    model (Books): The model to use for creating a new book record, which is the "Books" model.
    fields (list or str): The fields to include in the form for creating a new book record. In this case, all fields are included.
    success_url (str): The URL to redirect to upon successful book creation.

    Usage:
    - Create an instance of this view in your URL configuration to allow users to create new book records.
    """
    model = Books
    fields = "__all__"
    success_url = reverse_lazy("books:books-list")


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


class BooksUpdateView(UpdateView):
    model = Books
    template_name = 'books/books_update.html'  # Замените на ваш шаблон
    fields = ['title', 'author', 'year', 'description', 'cover']  # Укажите поля, которые можно редактировать

    def get_success_url(self):
        return reverse('books:books-detail', kwargs={'pk': self.object.pk})


class BooksDeleteView(DeleteView):
    """
      View for deleting a book record.

      Attributes:
      model (Books): The model from which to delete a book record, which is the "Books" model.
      success_url (str): The URL to redirect to after successfully deleting the book record.

      Usage:
      - Create an instance of this view in your URL configuration to allow users to delete book records.
      """
    model = Books
    success_url = reverse_lazy("books:books-list")
