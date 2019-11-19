from django.urls import path, include, reverse_lazy
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from .views import (
    ProfileUpdateView, CommunityLeaderListView, CommunityLeaderFormView, StreetLeaderListView,
    StreetLeaderFormView
)

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('reset/password-reset/', views.PasswordResetView.as_view(template_name='user/password_reset_form.html',
        email_template_name='user/password_reset_email.html', success_url = reverse_lazy('user:password_reset_done')),
        name='password_reset'),
    path('password-reset-done/', views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',
        success_url = reverse_lazy('user:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
        name='password_reset_complete'),
    path('password-change/', login_required(views.PasswordChangeView.as_view(template_name='user/password_change_form.html',
        success_url = reverse_lazy('user:password_change_done'))), name='password_change'),
    path('password-change-done/', login_required(views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html')),
        name='password_change_done'),

    path('profile/update/<int:pk>/', login_required(ProfileUpdateView.as_view()), name='profile_update'),
    path('community-leader/list/', login_required(CommunityLeaderListView.as_view()), name='community_leader_list'),
    path('community-leader/create/', login_required(CommunityLeaderFormView.as_view()), name='community_leader_create'),
    path('street-leader/list/', login_required(StreetLeaderListView.as_view()), name='street_leader_list'),
    path('street-leader/create/', login_required(StreetLeaderFormView.as_view()), name='street_leader_create'),
    #path('profile-create/', ProfileCreateView.as_view(), name='profile_create'),
    #path('profile-update/<int:pk>/', login_required(ProfileUpdateView.as_view()), name='profile_update'),
    #path('profile-detail/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail')
]
