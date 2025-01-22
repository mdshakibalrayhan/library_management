from django import forms
from books.models import BookReview
class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['review']