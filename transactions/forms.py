from .models import UserTranscations
from django import forms
from account.models import UserAccount

class UserDeposit(forms.ModelForm):
    deposite = forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = UserAccount
        fields = ['deposite']
