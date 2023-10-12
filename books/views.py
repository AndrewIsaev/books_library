# Create your views here.
from django.views.generic import ListView, DetailView

from books.models import Books, Authors


class BooksListView(ListView):
    model = Books
    context_object_name = "books"
    paginate_by = 3

    def get_queryset(self):
        return Books.objects.select_related("author").all()


class BooksDetailView(DetailView):
    model = Books
    context_object_name = "book"
