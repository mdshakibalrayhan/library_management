from django.shortcuts import render
from books.models import AllBooks
from account.models import UserAccount,User
from transactions.models import UserTranscations
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def profile_page(request,id):
    user_account = UserAccount.objects.get(user = request.user)
    
    transactions = UserTranscations.objects.filter(user_account = user_account)
    user = User.objects.get(pk=id)
    print("Authenticated user:", request.user)
    print("Is user authenticated:", request.user.is_authenticated)
    print("Session key:", request.session.session_key)


    return render(request,'profile.html',{'user' : user,'user_account':user_account,'transactions' : transactions})