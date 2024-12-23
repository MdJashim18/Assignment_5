from django.shortcuts import render, redirect, reverse
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from transactions.models import Deposit
from django.db.models import Sum
from books.models import Borrowing
from django.utils import timezone


# Create your views here.
def register(request):
    if request.method=='POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('profile')
    else:
        register_form = forms.RegistrationForm()
    return render(request,'register.html',{'form' : register_form,'type' : 'Sign Up' })



class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Loged in Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Loged in information incorrect')
        return super().form_invalid(form)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context



def profile(request):
    deposits = Deposit.objects.filter(user=request.user)
    return render(request, 'profile.html', {'deposits': deposits})


def view_deposite(request):
    deposits = Deposit.objects.filter(user=request.user)  # Get user's deposits
    total_deposit = deposits.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'View_deposite.html', {'deposits': deposits, 'total_deposit': total_deposit})
    


def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'Update_profile.html', {'form' : profile_form})

def pass_change(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user , data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form' : form})

def logout_view(request):
    logout(request)
    return redirect('homepage')




@login_required
def profile(request):
    borrowings = Borrowing.objects.filter(user=request.user).select_related('book')
    deposits = Deposit.objects.filter(user=request.user)
    total_deposit = deposits.aggregate(Sum('amount'))['amount__sum'] or 0

    borrow_details = []
    remaining_deposit = total_deposit

    for record in borrowings:
        deposit_used = record.book.price
        remaining_deposit -= deposit_used
        borrow_details.append({
            'id': record.id,  
            'book_id': record.book.id,
            'book_title': record.book.title,
            'book_price': record.book.price,
            'borrow_date': record.borrow_date,
            'return_date': record.return_date,
            'deposit_used': max(remaining_deposit, 0),
        })

    return render(request, 'profile.html', {
        'borrow_details': borrow_details,
        'total_deposit': total_deposit,
        'user': request.user,
    })





def return_book(request, borrowing_id):
    borrowing = Borrowing.objects.get(id=borrowing_id)

    if borrowing.return_date:  
        messages.error(request, 'This book has already been returned.')
        return redirect('profile')  

    
    borrowing.return_date = timezone.now()  
    borrowing.save()

   
    book_price = borrowing.book.price
    user_deposit = Deposit.objects.filter(user=request.user).first()  

    if user_deposit:
        user_deposit.amount += book_price
        user_deposit.save()

        messages.success(request, f'You have successfully returned the book. ${book_price} has been added back to your deposit.')
    else:
        messages.error(request, 'No deposit found for this user.')

    return redirect('profile')