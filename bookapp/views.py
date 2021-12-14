from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BookModel, Review
from django.db.models import Q  # new


# Create your views here.
class BookView(ListView):
    model = BookModel
    template_name = "Books/AllBooks.html"
    context_object_name = "Books"


class BookDetail(DetailView):
    model = BookModel
    template_name = "Books/oneBook.html"
    context_object_name = "Book"


class SearchResultsListView(ListView):
    model = BookModel
    template_name = "Books/AllBooks.html"
    context_object_name = "Books"

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return BookModel.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query))
