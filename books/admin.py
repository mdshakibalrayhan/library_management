from django.contrib import admin
from .models import AllBooks,Category,BookReview
# Register your models here.

admin.site.register(Category)
admin.site.register(AllBooks)
admin.site.register(BookReview)