from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView,  PasswordResetConfirmView, \
    PasswordResetCompleteView
from .forms import LoginForm

app_name = 'user'

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='user/login.html', form_class=LoginForm, redirect_authenticated_user=True),
         name='login'),
    path('Registration/', views.RegisterView.as_view(), name='Registration'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('addQuote/', views.add_quote, name='addQuote'),

    path('reset-password/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',
                                          success_url='/user/reset-password/complete/'),
         name='password_reset_confirm'),
    path('user/reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),
]
