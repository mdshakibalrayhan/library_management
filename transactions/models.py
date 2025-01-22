from django.db import models
from account.models import UserAccount
from books.models import AllBooks
from .constants import TRANSACTION_TYPE
# Create your models here.

class UserTranscations(models.Model):
    user_account = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=15)
    date = models.DateTimeField()
    book = models.ForeignKey(AllBooks,on_delete=models.CASCADE)
    paid_status = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return f"transaction record-{self.user_account.user.first_name}"
    

