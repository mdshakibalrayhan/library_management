from .import views
from django.urls import path
urlpatterns = [
    path('',views.home,name='home'),
    path('all_books/',views.All_books,name='all_books'),
    path('all_books/<slug:id>/',views.All_books,name='category_wise_book'),
    path('book_details/<int:id>/',views.BookDetailsView.as_view(),name='details'),
]