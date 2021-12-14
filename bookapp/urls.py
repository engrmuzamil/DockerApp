from django.urls import path
from .views import BookView, BookDetail, SearchResultsListView

urlpatterns = [
    path('', BookView.as_view(), name='book_list'),
    path('detail/<uuid:pk>/', BookDetail.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results')
]
