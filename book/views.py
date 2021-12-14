from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BookModel


# Create your views here.
class BookView(ListView):
    model = BookModel
    template_name = "Books/AllBooks.html"
    context_object_name = "Books"


class BookDetail(DetailView):
    model = BookModel
    template_name = "Books/oneBook.html"
    context_object_name = "Book"