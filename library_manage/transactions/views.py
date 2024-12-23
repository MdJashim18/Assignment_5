# In your app's views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DepositForm
from .models import Deposit

@login_required  
def deposit_money(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user 
            deposit.save()
            return redirect('profile')
    else:
        form = DepositForm()

    return render(request, 'deposite.html', {'form': form})
