from django.shortcuts import render,redirect
from books.models import AllBooks,Category,BookReview
from account.models import UserAccount
from django.views.generic.detail import DetailView
from transactions.models import UserTranscations
from .forms import ReviewForm

def home(request):
    if request.user.is_authenticated:
        user_account = UserAccount.objects.get(user=request.user)
        return render(request,'home.html',{'user_account':user_account})
    else:
        return render(request,'home.html')

def All_books(request,id = None):
    
    user_account = None
    categories = Category.objects.all()

    if request.user.is_authenticated:
        user_account = UserAccount.objects.get(user=request.user)
    if id:
        categories = Category.objects.get(id=id)
        books = AllBooks.objects.filter(Category=categories)
    else:
        books = AllBooks.objects.all()
    
    if user_account:
        return render(request,'all_books.html',{'books':books,'user_account':user_account,'categories':categories,'all_category':Category.objects.all()})
    return render(request,'all_books.html',{'books':books,'categories':categories,'all_category':Category.objects.all()})

def Is_purchased(user,book):
    trasactions = UserTranscations.objects.filter(user_account=user)
    trasactions = trasactions.filter(book=book)
    verify = False
    if trasactions:
        verify = True
    return verify

class BookDetailsView(DetailView):
    model = AllBooks
    template_name = 'book_details.html'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get(self.pk_url_kwarg)
        reviews = BookReview.objects.filter(book=book_id)
        print(reviews)
        data = self.get_object()
        context['data'] = data
        context['reviews'] = reviews
        if self.request.user.is_authenticated:
            if Is_purchased(UserAccount.objects.get(user=self.request.user),AllBooks.objects.get(id=book_id)):
                context['form'] = ReviewForm

        return context
    
    def post(self,request,*args,**kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.cleaned_data.get('review')
            user_account = UserAccount.objects.get(user=self.request.user)
            book_id = self.kwargs.get(self.pk_url_kwarg)
            book = AllBooks.objects.get(id=book_id)

            BookReview.objects.create(
                user=user_account,
                review = review,
                book = book
            )
        return redirect('details',id=book.id)