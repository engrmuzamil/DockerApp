from django.urls import path
from .views import BookView, BookDetail

urlpatterns = [
    path('', BookView.as_view(), name='book_list'),
    path('detail/<uuid:pk>/', BookDetail.as_view(), name='book_detail'),
]
