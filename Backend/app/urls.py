from django.urls import path

from app.views import authentication
from app.views.login import CustomTokenObtainPairView
from app.views.admin import AdminView
from app.views.users import *
from app.views.dpi import *
from app.views.soins import *

urlpatterns = [
    path('POST/', authentication.index_POST, name='index_POST'),
    path('GET/', authentication.index_GET, name='index_GET'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('SignUp/', authentication.SignUp, name='SignUp'),
    path('token_test/', authentication.token_test, name='token_test'),
    path('users/add/', RegisterView.as_view(), name="register_view"),
    path('dpi/add/', AddDPIView.as_view(), name="add_dpi_view"),
    path('soins/add/', AddSoinView.as_view(), name="add_soins"),
    path('soins/', ListSoinsView.as_view(), name="list_soins"),
    path('users/', ListUsersView.as_view(), name="list_users"),
    path('dpi/', ListDPIsView.as_view(), name="list_dpis"),
    path('users/<int:pk>/', GetUserView.as_view(), name="get_user"),
    path('dpi/<int:pk>/', GetDPIView.as_view(), name="get_dpi"),
    path('soins/<int:pk>/', GetSoinView.as_view(), name="get_soin"),
]