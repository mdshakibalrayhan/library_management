from django.db import models
from account.models import UserAccount
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class AllBooks(models.Model):
    titel = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    borrwing_price = models.DecimalField(max_digits=12,decimal_places=2)
    Category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='books/uploads')

    def __str__(self):
        return self.titel
    

class BookReview(models.Model):
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    review = models.CharField(max_length=300)
    book = models.ForeignKey(AllBooks,on_delete=models.CASCADE)

    def __str__(self):
        return f"Review of {self.book} by {self.user}"