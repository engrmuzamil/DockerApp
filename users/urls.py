from django.contrib.auth import views
from django.urls import path
from .views import SignupPageView
# Create your views here.
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', SignupPageView.as_view(), name='signup'),
]
