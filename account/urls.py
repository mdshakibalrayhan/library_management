
from django.urls import path
from .views import RegistrationView,UserLoginView,UserLogoutView

urlpatterns = [
    path('register/',RegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
]
