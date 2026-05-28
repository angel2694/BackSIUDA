from .views import AssignRoleAPIView, LoginAPIView, ProfileAPIView, UserListAPIView, test_protected, RegisterAPIView, ChangePasswordAPIView, PasswordResetRequestAPIView, PasswordResetConfirmAPIView
from django.urls import path

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:id>/role/', AssignRoleAPIView.as_view(), name='assign-role'),
    path('test/', test_protected, name='test-protected'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('profile/password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password-reset-request'),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name='password-reset-confirm'),
]
