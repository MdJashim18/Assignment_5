from transactions.models import Deposit
from django.db.models import Sum

def deposit_balance(request):
    if request.user.is_authenticated:
        total_deposit = Deposit.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
        print(f"User: {request.user}, Total Deposit: {total_deposit}")  # Debug
    else:
        total_deposit = 0
        print("User not authenticated")
    return {'total_deposit': total_deposit}

