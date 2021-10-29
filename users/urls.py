from django.urls import path
from rest_framework.views import csrf_exempt
from .views import UserRegistration, UserAuthentication, get_user, user_logout


urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserAuthentication.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('get_user/', get_user, name='get_user')
]