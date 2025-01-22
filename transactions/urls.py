
from django.urls import path
from .import views
urlpatterns = [
    path('transactios/<int:id>',views.BorrowBook,name='transaction'),
    path('deposit/',views.user_deposit,name='deposit'),
    path('return_book/',views.ReturnBookPage,name='return_book'),
    path('return/<int:id>/',views.Return_Book,name='return'),
]
