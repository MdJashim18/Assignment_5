from django.urls import path
from .views import DetailsPostView
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('detail/<int:pk>/', DetailsPostView.as_view(), name='details_post'),
    path('book/<int:book_id>/buy/', views.borrow_book, name='buy_book'),
    path('buy/result/', views.buy_result, name='buy_result'),
    path('buy/failed/', views.buy_failed, name='buy_failed'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)