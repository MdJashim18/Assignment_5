from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import Book, Category,Borrowing
from django.shortcuts import redirect
from django.views import View
from .models import Book
from .import models,forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from transactions.models import Deposit
from django.db.models import Sum
from django.contrib import messages

# Create your views here.

MIN_DEPOSIT_REQUIRED = 100 
@method_decorator(login_required, name='dispatch')
class DetailsPostView(DetailView):
    model = Book
    template_name = 'book_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()  
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = self.get_object()
        context['comments'] = self.object.comments.all()
        context['comment_form'] = forms.CommentForm()
        return context

    
    
@login_required
def borrow_book(request, book_id):
    deposits = Deposit.objects.filter(user=request.user)
    total_deposit = deposits.aggregate(Sum('amount'))['amount__sum'] or 0
    book = Book.objects.get(id=book_id)
    if total_deposit < book.price:
        messages.error(request, f"You need at least {book.price} USD in deposits to borrow a book.")
        return redirect('buy_failed')
    
    
    
   
    if book.quantity > 0:
        remaining_price = book.price
        for deposit in deposits:
            if deposit.amount >= remaining_price:
                deposit.amount -= remaining_price
                deposit.save()
                break
            else:
                remaining_price -= deposit.amount
                deposit.amount = 0
                deposit.save()
        
        Borrowing.objects.create(user=request.user, book=book)
        book.quantity -= 1  
        if book.quantity == 0:
            book.is_available = False 
        book.save()
        messages.success(request, f"You have successfully borrowed '{book.title}'!")
    else:
        messages.error(request, f"Sorry, '{book.title}' is currently not available.")

    return redirect('buy_result') 



def buy_result(request):
    return render(request, 'Borrow_result.html')
def buy_failed(request):
    return render(request, 'Buy_failed.html')


