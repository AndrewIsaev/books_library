# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from books.forms import CommentsForm
from books.models import Books, Comments


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
        Return the queryset of books, including related author information and search results.

        If a search query is provided in the URL parameters, filter the queryset based on the query.
        """
        query = self.request.GET.get('q', '')
        queryset = Books.objects.select_related("author")

        if query:
            # Filter the queryset based on the search query for book title or author name
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(author__name__icontains=query)
            )

        return queryset


class BooksCreateView(LoginRequiredMixin, CreateView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.select_related("user")
        context['comment_form'] = CommentsForm()  # Добавляем форму в контекст
        return context


class BooksUpdateView(LoginRequiredMixin, UpdateView):
    model = Books
    template_name = 'books/books_update.html'  # Замените на ваш шаблон
    fields = ['title', 'author', 'year', 'description', 'cover']  # Укажите поля, которые можно редактировать

    def get_success_url(self):
        return reverse('books:books-detail', kwargs={'pk': self.object.pk})


class BooksDeleteView(LoginRequiredMixin, DeleteView):
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


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CommentsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book_id = self.kwargs['book_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('books:books-detail', args=[self.kwargs['book_id']])
