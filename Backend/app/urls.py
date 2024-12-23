from django.urls import path

from app.views import authentication
from app.views.login import CustomTokenObtainPairView
from app.views.admin import AdminView
from app.views.register import RegisterView

urlpatterns = [
    path('POST/', authentication.index_POST, name='index_POST'),
    path('GET/', authentication.index_GET, name='index_GET'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('SignUp/', authentication.SignUp, name='SignUp'),
    path('token_test/', authentication.token_test, name='token_test'),
    path('users/add', RegisterView.as_view(), name="register_view")
]