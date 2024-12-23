
from . import views
from django.urls import path
urlpatterns = [
    path('deposit/', views.deposit_money, name='deposit_money'),
]
