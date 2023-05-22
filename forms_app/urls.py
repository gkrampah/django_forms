from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="forms_app-index"),
    path("profile/", views.profile, name="forms_app-profile"),
    path("register/", views.register, name="forms_app-register"),
    path('login/', auth_views.LoginView.as_view(template_name='forms_app/login.html'), name='forms_app-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='forms_app/logout.html'), name='forms_app-logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='forms_app/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='forms_app/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='forms_app/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='forms_app/password_reset_complete.html'
         ),
         name='password_reset_complete'),
      
  
]