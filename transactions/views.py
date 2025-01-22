from django.shortcuts import render,redirect
from books.models import AllBooks
from account.models import UserAccount
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import UserDeposit
from django.shortcuts import get_object_or_404
from decimal import Decimal,InvalidOperation
from .models import UserTranscations
from .constants import BORROWING,RETURNING
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

def send_transaction_email(user, amount, subject, template,book_or_account):

        message = render_to_string(template, {
        'user' : user,
        'amount' : amount,
        'book_account' : book_or_account,
        })

        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

def BorrowBook(request,id):
    book = AllBooks.objects.get(pk=id)
    user = UserAccount.objects.get(user=request.user)

    if book.borrwing_price > user.deposite:
        message = 'Your account balance is less than the book price, you are not allowed to borrow this book!!'
        return render(request,'borrow_book.html',{'data':message})
    else:
        user.deposite -= book.borrwing_price
        user.save()
        
        UserTranscations.objects.create(
            user_account = user,
            book = book,
            transaction_type = 'BORROWING',
            date = timezone.now(),
            paid_status = False,
        )

        message = f' Hi {user.user.first_name} Your borriwing is successfull. Your cuurent balance is {user.deposite}.'
        send_transaction_email(request.user,book.borrwing_price,'Borrowing email','borrowing_email.html',book)
    
    return redirect('home')

@login_required
def ReturnBookPage(request):
    user_account = UserAccount.objects.get(user=request.user)
    transactions = UserTranscations.objects.filter(user_account=user_account)
    transactions = transactions.filter(paid_status=False)
    print(transactions)
    return render(request,'return_book.html',{'books':transactions})

def Return_Book(request,id):

    transaction_record = UserTranscations.objects.get(id=id)
    user_account = UserAccount.objects.get(id=transaction_record.user_account.id)

    book = AllBooks.objects.get(id=transaction_record.book.id)
    transaction_record.paid_status = True
    print(user_account.deposite)
    print(book.borrwing_price)
    user_account.deposite += Decimal(book.borrwing_price)
    print(user_account.deposite)
    user_account.save(update_fields=['deposite'])
    transaction_record.save()
    send_transaction_email(request.user,book.borrwing_price,'RETRUNING BOOK','return_amount_email.html',book)

    return redirect('home')

def user_deposit(request):
    user = UserAccount.objects.get(user=request.user)
    print(user.deposite)
    if request.method == 'POST':
        form = UserDeposit(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['deposite']
            send_transaction_email(request.user,amount,"Deposit",'deposit_email.html',user)
            user.deposite += amount
            user.save()
            return redirect('home')
    else:
        form = UserDeposit()
    return render(request,'deposit.html',{'form':form})
        

    