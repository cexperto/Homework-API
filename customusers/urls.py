from .views import SignUpView, LoginView, UserAPIView, RefreshAPIView
from django.urls import path

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshAPIView.as_view(), name='refresh'),
    path('user/', UserAPIView.as_view(), name='user')
]