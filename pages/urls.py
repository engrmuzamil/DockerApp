from .views import homeView, aboutView
from django.urls import path

urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('about/', aboutView.as_view(), name="about"),
]
