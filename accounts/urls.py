from .views import AssignRoleAPIView, LoginAPIView, test_protected
from django.urls import path

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/<int:id>/role/', AssignRoleAPIView.as_view(), name='assign-role'),
    path('test/', test_protected, name='test-protected'),
]   