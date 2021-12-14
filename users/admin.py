from django.contrib import admin
from .forms import CustChangeForm, CustCreateForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

Users = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustCreateForm
    form = CustChangeForm
    model = Users
    list_display = ["username", "email"]


admin.site.register(Users, CustomUserAdmin)
