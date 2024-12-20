from django.urls import path

from app.views import authentication

urlpatterns = [
    path('POST/', authentication.index_POST, name='index_POST'),
    path('GET/', authentication.index_GET, name='index_GET'),
    path('Login/', authentication.Login, name='Login'),
    path('SignUp/', authentication.SignUp, name='SignUp'),
    path('token_test/', authentication.token_test, name='token_test'),
]