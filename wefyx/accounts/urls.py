from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Auth-related
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Profile
    path('edit/', views.edit_profile_view, name='profileEdit'),

    # Settings and help
    path('settings/', views.settings_view, name='settings'),
    path('help/', views.help_view, name='help'),

    # Posts
    path('post/', views.post_upload_view, name='postUpload'),
    path('follow-toggle/', views.follow_toggle_view, name='follow_toggle'),

    # Password reset flow
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/registration/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/registration/password_reset_complete.html'), name='password_reset_complete'),

]
