from django.shortcuts import render,redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.contrib.auth import login,logout
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

class RegistrationView(FormView):
    template_name = 'account/registration_form.html'
    success_url = reverse_lazy('home')
    form_class = RegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "account/login.html"
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect(reverse_lazy('home'))