from .views import LoginAPIView, test_protected
from django.urls import path

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('test/', test_protected, name='test-protected')
]   