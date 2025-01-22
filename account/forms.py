from django import forms
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .constants import GENDER_TYPE


class RegistrationForm(UserCreationForm):
    user_address = forms.CharField(max_length=150)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    deposite = forms.DecimalField(max_digits=5,decimal_places=2)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','user_address','birth_date','gender','deposite']

    def save(self,commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()

            user_address = self.cleaned_data.get('user_address')
            gender = self.cleaned_data.get('gender')
            birth_date = self.cleaned_data.get('birth_date')
            deposite = self.cleaned_data.get('deposite')

            UserAccount.objects.create(
                user = our_user,
                user_address = user_address,
                gender = gender,
                birth_date = birth_date,
                deposite = deposite
            )
        return our_user