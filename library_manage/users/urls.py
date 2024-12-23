from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/' , views.edit_profile,name='edit_profile'),
    path('profile/edit/pass_change/' , views.pass_change,name='pass_change'),
    path('logout/', views.logout_view, name='logout'),
    path('view_deposite/', views.view_deposite, name='view_deposite'),
    path('return_book/<int:borrowing_id>/', views.return_book, name='return_book'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)