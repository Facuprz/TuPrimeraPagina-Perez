from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    path('login/',  LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('password/change/',
         PasswordChangeView.as_view(
            template_name='accounts/password_change.html',
            success_url=reverse_lazy('profile')
         ),
         name='password_change'),
]
