from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustCreateForm(UserCreationForm):
    model = get_user_model()
    fields = ("username", "email")


class CustChangeForm(UserChangeForm):
    model = get_user_model()
    fields = ("username", "email")