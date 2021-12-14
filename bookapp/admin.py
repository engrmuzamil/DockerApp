from django.contrib import admin
from .models import BookModel, Review


class ReviewInline(admin.TabularInline):
    model = Review


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ('title', 'author', 'price')


admin.site.register(BookModel, BookAdmin)
admin.site.register(Review)