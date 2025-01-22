from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    user_address = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    deposite = models.DecimalField(max_digits=12,decimal_places=2,default=0,null=True,blank=True)

    def __str__(self):
        return str(self.user.first_name)