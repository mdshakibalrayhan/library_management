from .import views
from django.urls import path
urlpatterns = [
        path('profile_page/<int:id>/',views.profile_page,name='profile'),
]